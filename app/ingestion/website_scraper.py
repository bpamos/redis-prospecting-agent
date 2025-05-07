# import requests
# from bs4 import BeautifulSoup

# def scrape_website(url: str) -> str:
#     """Scrapes and returns visible text from a website."""
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
#     }

#     try:
#         response = requests.get(url, headers=headers, timeout=10)
#         response.raise_for_status()
#     except Exception as e:
#         raise RuntimeError(f"Failed to fetch website: {e}")

#     soup = BeautifulSoup(response.text, "html.parser")

#     # Remove script/style tags
#     for tag in soup(["script", "style", "noscript"]):
#         tag.decompose()

#     return soup.get_text(separator=" ", strip=True)

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def is_valid_link(link, domain):
    parsed = urlparse(link)
    return (
        parsed.netloc == domain or parsed.netloc == ""
    ) and not any(skip in link for skip in ["#", "mailto:", "tel:", ".pdf", ".zip", "/blog", "/careers"])

def extract_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)

def crawl_website(root_url: str, max_pages: int = 10) -> str:
    visited = set()
    to_visit = [root_url]
    collected_text = []

    parsed_root = urlparse(root_url)
    base_domain = parsed_root.netloc

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
        except Exception as e:
            print(f"⚠️ Skipping {url}: {e}")
            continue

        visited.add(url)
        print(f"✅ Crawled: {url}")

        text = extract_text(response.text)
        if len(text) > 100:
            collected_text.append(text)

        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a", href=True):
            href = urljoin(url, link["href"])
            if is_valid_link(href, base_domain) and href not in visited and href not in to_visit:
                to_visit.append(href)

    return "\n\n".join(collected_text)
