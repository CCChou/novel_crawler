# Novel Crawler

Tools for crawling the novels, currently support the following websites.
* [UU看書](https://tw.uukanshu.com/)
* [鉛筆小說](https://www.x23qb.com/)
* [小說狂人](https://czbooks.net)

## Usage

Setup Virtual Environment
```
pip -m venv .venv
source .venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

Install current project as well
```
pip install -e .
```

Modify the config.json, change the save directory
```
{
  "store_dir" : "C:\\path\\you\\want\\to\\save\\novels",
  "file_format" : "txt"
}
```

Execute the crawler
```
python novel_crawler/main.py [novel_url]
```
