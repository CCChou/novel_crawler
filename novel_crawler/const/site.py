from enum import Enum


class StrEnum(str, Enum):
    pass


class Site(StrEnum):
    UU = 'https://tw.uukanshu.com'
    CZ = 'https://czbooks.net'

    def get_base(self):
        return self.value + '/{}'
