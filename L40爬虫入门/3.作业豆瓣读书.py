# 豆瓣读书新书速递书名作者爬取

import urllib.request
from fake_useragent import UserAgent
import random
import re, requests

res = requests.get(
    url = 'https://book.douban.com/',
    headers ={
    'User-Agent': UserAgent().random}
).text
# req = urllib.request.Request(base_url, headers=headers)
# resp = urllib.request.urlopen(req)
# html_content = resp.read().decode('utf-8')
# print(html_content)


pattern = re.compile(r'<div class="more-meta">.*?<h4.*?>(.*?)</h4>.*?<span class="author">(.*?)</span>', re.S)
results =re.findall(pattern, res)
print(results)
for row in results:
    print(row.strip())