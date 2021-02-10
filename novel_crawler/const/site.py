from enum import Enum


class StrEnum(str, Enum):
    pass


class Site(StrEnum):
    UU = 'https://tw.uukanshu.com'
    CZ = 'https://czbooks.net'
    X23QB = 'https://www.x23qb.com'

    def get_base(self):
        return self.value + '{}'
