from ebooklib import epub

book = epub.EpubBook()

book.set_identifier('test123')
book.set_title('Test book')
book.set_language('zh-TW')

c1 = epub.EpubHtml(title='Chapter01', file_name='chap_01.xhtml', lang='zh-TW')
c1.connect = u'<h1>Chapter01</h1><p>This is chapter 01 for test</p>'

book.add_item(c1)

book.toc = (epub.Link('chap_01.xhtml', 'Chapter01', 'ch01'), (epub.Section('Simple Book'), (c1, )))

book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

style = 'BODY {color: white;}'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

book.add_item(nav_css)

book.spine = ['nav', c1]

epub.write_epub('test.epub', book, {})
