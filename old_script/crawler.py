import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", 
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

with open("D:\\test.txt", "a", encoding='utf8') as file:
    # 妖刀記
    baseUrl = "http://m.123xiaoqiang.net/15_15566/{}"
    index = 1013119
    for i in range(0, 8):
        threadId = str(i + index) + ".html"
        while threadId:
            url = baseUrl.format(threadId)
            req = session.get(url, headers=headers)
            html = req.text.encode("iso-8859-1")
            
            htmlPage = BeautifulSoup(html, "html.parser")
            content = htmlPage.select_one("#chaptercontent")
            excludePageTag = htmlPage.select_one(".chapterPages")
            nextPage = htmlPage.select_one(".curr + a")

            if(nextPage):
                threadId = nextPage.get("href")
            else:
                threadId = None

            excludePageTag.decompose()
            cleanContent = content.get_text("\n", "<br/>").replace("『加入书签，方便阅读』", "")
            file.write(cleanContent)
