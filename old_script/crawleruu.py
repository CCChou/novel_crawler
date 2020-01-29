# UU 仙子請自重 b/92369/21254.html
# UU 放浪形骸歌 b/72742/14317.html
# UU 降魔專家 b/115037/1248.html

import requests
import re
from bs4 import BeautifulSoup


def main():
    # 不好，抓資料和儲存應該切開，目前這樣不符合單一職責原則
    with open('D:\\test.txt', 'a', encoding='utf8') as file:
        base_url = 'https://www.uukanshu.com/{}'
        index = 'b/115037/1248.html'

        while index and '.html' in index:
            url = base_url.format(index)

            print(url)

            html = get_html(url)
            html_page = BeautifulSoup(html, 'lxml')
            # 缺防呆
            index = html_page.select_one('#next').get('href')
            title = html_page.select_one('#timu').get_text()
            content = html_page.select_one('#contentbox').get_text('\n', '<p>')
            clean_content = get_clear_content(content)

            print(title)

            file.write(title)
            file.write("\n\n")
            file.write(clean_content)
            file.write("\n\n")


def get_html(url):
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    req = session.get(url, headers=headers)
    return req.text


def get_clear_content(content):
    return re.sub(
        '[UＵwｗaａcｃhｈkｋmｍnｎoｏsｓuｕwｗ.．]{2}看书[\s]*[UＵwｗaａcｃhｈkｋmｍnｎoｏsｓuｕwｗ.．]+|\(adsbygoogle = window.adsbygoogle \|\| '
        '\[\]\).push\({}\);',
        '', content)


if __name__ == '__main__':
    main()
