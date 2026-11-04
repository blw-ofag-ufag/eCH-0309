import subprocess
import re
from pathlib import Path
import urllib.request
import urllib.error
import pytest
import time

def get_tracked_files():
    """Returns a list of .md, .qmd, .bib and CSL YAML files tracked by git, falling back to rglob if git fails."""
    try:
        result = subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True, check=True)
        files = [f for f in result.stdout.split('\0') if f and f.endswith(('.md', '.qmd', '.bib', '.yaml'))]
        return [Path(f) for f in files]
        
    except (subprocess.SubprocessError, FileNotFoundError):
        files = []
        for ext in ("*.md", "*.qmd", "*.bib", "*.yaml"):
            files.extend(
                p for p in Path(".").rglob(ext)
                if not set(p.parts) & {"venv", "build", ".quarto", ".git"}
            )
        return files

def get_urls():
    """Extract URLs from all tracked Markdown, BibTeX and CSL YAML files, ignoring code blocks in Markdown."""
    url_regex = re.compile(r'\[[^\]]*\]\((https?://[^\)]+)\)')
    url_regex_angle = re.compile(r'<(https?://[^>]+)>')
    bib_url_regex = re.compile(r'(?i)\burl\s*=\s*[{"]\s*(https?://[^"\}]+)\s*["\}]')
    csl_url_regex = re.compile(r'^\s*URL:\s*"?(https?://[^\s"]+)', re.MULTILINE)
    
    urls = []
    for f in get_tracked_files():
        if not f.exists():
            continue
            
        content = f.read_text(encoding="utf-8")
        
        if f.suffix.lower() in ('.md', '.qmd'):
            content_no_code = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
            content_no_code = re.sub(r'`[^`]*`', '', content_no_code)
    
            for match in url_regex.finditer(content_no_code):
                urls.append((str(f), match.group(1)))
            for match in url_regex_angle.finditer(content_no_code):
                urls.append((str(f), match.group(1)))
                
        elif f.suffix.lower() == '.bib':
            for match in bib_url_regex.finditer(content):
                urls.append((str(f), match.group(1).strip()))

        elif f.suffix.lower() == '.yaml':
            for match in csl_url_regex.finditer(content):
                urls.append((str(f), match.group(1)))

    return sorted(list(set(urls)))

@pytest.mark.parametrize("file_path, url", get_urls())
def test_document_link(file_path, url):
    """Checks the HTTP status code of referenced external URLs with retries."""
    # An honest User-Agent and an explicit Accept. The spoofed browser string
    # this used to send tripped the bot protection on news.admin.ch, and the
    # missing Accept made the fedlex ELI endpoint answer 400 to every request.
    req = urllib.request.Request(url, headers={
        'User-Agent': 'eCH-0309-link-check/1.0 (+https://github.com/blw-ofag-ufag/eCH-0309)',
        'Accept': '*/*',
    })
    
    max_retries = 3
    delay_between_retries = 2

    for attempt in range(max_retries):
        try:
            req.get_method = lambda: 'HEAD'
            urllib.request.urlopen(req, timeout=10)
            return
            
        except urllib.error.HTTPError as e:
            if e.code in (405, 403, 401):
                try:
                    req.get_method = lambda: 'GET'
                    urllib.request.urlopen(req, timeout=10)
                    return
                    
                except urllib.error.HTTPError as e2:
                    pytest.fail(f"HTTPError {e2.code} for {url} in {file_path}")
                except Exception as e2:
                    last_exception = e2
            else:
                pytest.fail(f"HTTPError {e.code} for {url} in {file_path}")
                
        except Exception as e:
            last_exception = e
            
        if attempt < max_retries - 1:
            time.sleep(delay_between_retries)
            
    pytest.skip(f"No response from server after {max_retries} attempts. Reason: {last_exception}")