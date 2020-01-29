from novel_crawler.crawler.uucralwer import UUCrawler
from novel_crawler.const.site import Site


class CrawlerProvider:
    @staticmethod
    def create_crawler(url: str):
        if url.startswith(Site.UU.value):
            return UUCrawler(url)
