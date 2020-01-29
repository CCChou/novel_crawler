class Document:
    def __init__(self, order, title, content):
        self.__order = order
        self.__title = title
        self.__content = content

    @property
    def order(self):
        return self.__order

    @property
    def title(self):
        return self.__title

    @property
    def content(self):
        return self.__content
