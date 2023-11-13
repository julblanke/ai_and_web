import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class Crawler:

    def __init__(self, url: str):
        self.url = url

    def crawl(self):
        # Start URL and server information
        parsed_base_url = urlparse(self.url)

        # Set to keep track of visited URLs
        visited_urls = set()

        # Queue for URLs to be crawled
        url_queue = [self.url]

        # Crawl loop
        while url_queue:
            current_url = url_queue.pop(0)

            if current_url not in visited_urls:
                print(f"Crawling: {current_url}")
                visited_urls.add(current_url)

                html = self._fetch_and_parse(current_url=current_url)
                if html:
                    # Process the HTML content here
                    # You can add your processing logic

                    # Extract links from the page
                    links = self._extract_links(html, current_url, parsed_base_url=parsed_base_url)

                    # Add new links to the queue
                    url_queue.extend(links)

    def _fetch_and_parse(self, current_url):
        try:
            response = requests.get(current_url, timeout=60)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {current_url}: {e}")
        return None

    def _extract_links(self, html, base_url, parsed_base_url):
        links = set()
        soup = BeautifulSoup(html, 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            absolute_url = urljoin(base_url, href)
            parsed_url = urlparse(absolute_url)
            # Check if the link is on the same server
            if parsed_url.netloc == parsed_base_url.netloc:
                links.add(absolute_url)
        return links
