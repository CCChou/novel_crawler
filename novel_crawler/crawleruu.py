# UU 仙子請自重 b/92369/21254.html
# UU 放浪形骸歌 b/72742/14317.html

import requests
import re
from bs4 import BeautifulSoup

def main():
    # 不好，抓資料和儲存應該切開，目前這樣不符合單一職責原則
    with open("D:\\test.txt", "a", encoding='utf8') as file:
        baseUrl = "https://www.uukanshu.com/{}"
        index = "b/92369/100963.html"

        while index and '.html' in index:
            url = baseUrl.format(index)

            print(url)

            html = get_html(url)
            htmlPage = BeautifulSoup(html, "lxml")
            # 缺防呆
            index = htmlPage.select_one("#next").get("href")
            title = htmlPage.select_one("#timu").get_text()
            content = htmlPage.select_one("#contentbox").get_text("\n", "<p>")
            cleanContent = getClearContent(content)

            print(title)

            file.write(title)
            file.write("\n\n")
            file.write(cleanContent)
            file.write("\n\n")
            

def get_html(url):
    session = requests.Session()
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", 
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }

    req = session.get(url, headers=headers)
    return req.text

def getClearContent(content):
    return re.sub("[UＵwｗaａcｃhｈkｋmｍnｎoｏsｓuｕwｗ.．]{2}看书[\s]*[UＵwｗaａcｃhｈkｋmｍnｎoｏsｓuｕwｗ.．]+|\(adsbygoogle = window.adsbygoogle \|\| \[\]\).push\({}\);", "", content)

if __name__ == '__main__':
    main()