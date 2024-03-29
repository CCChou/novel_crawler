from abc import abstractmethod, ABCMeta

from novel_crawler.model.document import Document


class FileDao(metaclass=ABCMeta):
    def __init__(self, base_path):
        self._base_path = base_path

    def save(self, document: Document):
        with open(self._get_temp_file_path(document.order), 'w', encoding='utf8') as file:
            file.write(document.title)
            file.write('\n\n')
            file.write(document.content)
            file.write('\n\n')

    def _get_temp_file_path(self, index):
        return self._base_path + str(index)

    @abstractmethod
    def union(self, name, size):
        pass
