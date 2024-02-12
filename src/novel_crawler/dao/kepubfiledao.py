import os
import subprocess

from novel_crawler.dao.epubfiledao import EpubFileDao


class KepubFileDao(EpubFileDao):
    def union(self, name, size):
        super().union(name, size)
        file_name = self._get_valid_name(name)
        subprocess.check_call(['../lib/kepubify.exe', self._base_path + file_name + '.epub', '-o', self._base_path])
        os.remove(self._base_path + file_name + '.epub')
