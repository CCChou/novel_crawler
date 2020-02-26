from novel_crawler.crawler.uucralwer import UUCrawler
from novel_crawler.crawler.czcralwer import CZCrawler
from novel_crawler.const.site import Site


class CrawlerProvider:
    @staticmethod
    def create_crawler(url: str):
        if url.startswith(Site.UU.value):
            return UUCrawler(url)
        elif url.startswith(Site.CZ.value):
            return CZCrawler(url)
