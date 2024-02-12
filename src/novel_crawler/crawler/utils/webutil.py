import requests
from requests import RequestException


def get_html(url, encode=None, timeout=60, retry=5):
    count = 0
    while count < retry:
        try:
            session = requests.Session()
            headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
                          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            }
            req = session.get(url, headers=headers, timeout=timeout)
            if encode is not None:
                req.encoding = encode
            break
        except RequestException:
            count += 1
    return req.text
