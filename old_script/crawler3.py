# popo 非人 - 燼霖
import time
import requests
from bs4 import BeautifulSoup

account = "dses5900"
password = "gary0223chou"
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}


def main():
    login()

    index = 0

    with open("D:\\test.txt", "a", encoding='utf8') as file:
        baseUrl = "https://www.popo.tw{}"
        nextHref = '/books/583771/articles/6836780'  # "/books/583771/articles/6772370"
        while nextHref:
            url = baseUrl.format(nextHref)

            print(url)

            req = session.get(url, headers=headers)
            html = req.text
            htmlPage = BeautifulSoup(html, "html.parser")
            content = htmlPage.select_one("#readmask").get_text("\n", "</p>")
            nextPage = htmlPage.select_one(".next")

            if (nextPage):
                nextHref = nextPage.get("href")
            else:
                nextHref = None

            file.write(content)
            file.write('\n\n')

            index += 1
            time.sleep(2)
            # if (index % 10 == 0):
            #     time.sleep(10)


def login():
    login_param = {
        "account": account,
        "pwd": password,
        "remember_me": "1",
        "comefrom_id": "0",
        "owner": "COC",
        "front_events_id": "",
        "front_events_name": "",
        "client_ip": "122.118.6.23",
        "url": "https://www.popo.tw"
    }
    session.post("https://members.popo.tw/apps/login.php", headers=headers, data=login_param)


if __name__ == '__main__':
    main()
