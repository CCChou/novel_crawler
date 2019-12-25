class Document:
    def __init__(self, title, content, nextIndex):
        self._title = title
        self._content = content
        self._nextIndex = nextIndex
    
    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def nextIndex(self):
        return self._nextIndex

    def __str__(self):
        return f'{self._nextIndex}, {self._title}, {self._content}'