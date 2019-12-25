import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", 
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

with open("D:\\test.txt", "a", encoding='utf8') as file:
    # 逍遙小散仙
    baseUrl = "http://www.xiaoqiangwx.com/5/5000/{}.html"
    index = 335169
    for i in range(0, 10):
        url = baseUrl.format(index + i)
        req = session.get(url, headers=headers)
        html = req.text.encode("iso-8859-1")
        
        htmlPage = BeautifulSoup(html, "html.parser")
        content = htmlPage.select_one("#content")

        cleanContent = content.get_text("\n", "<br/>")
        file.write(cleanContent)
