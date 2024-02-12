import re
import os
from novel_crawler.dao.filedao import FileDao


class TxtFileDao(FileDao):
    def union(self, name, size):
        with open(self._base_path + self.__get_valid_name(name) + '.txt', 'w', encoding='utf8') as file:
            for index in range(1, size + 1):
                file.write(self.__read_content(index))
                file.write('\n\n')

    def __get_valid_name(self, name):
        return re.sub('[:]', '', name)

    def __read_content(self, index):
        path = self._get_temp_file_path(index)
        with open(path, 'r', encoding='utf8') as file:
            content = file.read()
        os.remove(path)
        return content
