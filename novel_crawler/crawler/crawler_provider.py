from novel_crawler.crawler.uucralwer import UUCrawler
from novel_crawler.crawler.czcralwer import CZCrawler
from novel_crawler.const.site import Site
from novel_crawler.crawler.x23qbcrawler import X23qbCrawler


class CrawlerProvider:
    @staticmethod
    def create_crawler(url: str):
        if url.startswith(Site.UU.value):
            return UUCrawler(url)
        elif url.startswith(Site.CZ.value):
            return CZCrawler(url)
        elif url.startswith(Site.X23QB.value):
            return X23qbCrawler(url)
        else:
            raise Exception("Unsupported url")
