# https://www.wenku8.net/novel/1/1213/index.htm

import requests
import re
from bs4 import BeautifulSoup
from document import Document

def exec():
    with open("D:\\test.txt", "a", encoding='utf8') as file:
        baseUrl = "https://www.wenku8.net/novel/1/1213/{}"
        index = "37500.htm"
        while index:
            url = baseUrl.format(index)
            doc = get_document(url)
            index = doc.nextIndex

            print(f'{doc.nextIndex}, {doc.title}')

            file.write(doc.title)
            file.write("\n\n")
            file.write(doc.content)
            file.write("\n\n")
            
def get_document(url):
    html = get_html(url)
    htmlPage = BeautifulSoup(html, "lxml")
    index = get_index(htmlPage)
    title = get_title(htmlPage)
    content = get_content(htmlPage)
    return Document(title, content, index)

def get_index(html):
    a_tags = html.select("#foottext > a")
    for a_tag in a_tags:
        if a_tag.get_text() == '下一页' and a_tag.get('href').endswith('htm'):
            return a_tag.get('href')
    return ''

def get_title(html):
    return html.select_one("#title").get_text()

def get_content(html):
    return html.select_one("#content").get_text("\n", "<p>")

def get_html(url):
    session = requests.Session()
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", 
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    req = session.get(url, headers=headers)
    req.encoding = 'gbk'
    return req.text

if __name__ == '__main__':
    exec()