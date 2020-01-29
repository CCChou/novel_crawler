from abc import ABCMeta, abstractmethod
from novel_crawler.model.source import Source


class Crawler(metaclass=ABCMeta):
    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url

    @abstractmethod
    def get_links(self):
        pass

    @abstractmethod
    def get_document(self, source: Source):
        pass
