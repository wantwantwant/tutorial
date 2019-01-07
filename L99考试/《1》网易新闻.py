# -*- coding: utf-8 -*-
# @Author: cyb

import urllib.request
from fake_useragent import UserAgent
import random
import re, requests
from lxml import etree

res = requests.get(
    url ='https://news.163.com/',
    headers ={
        'User-Agent': UserAgent().random}
).text

pattern = re.compile(r'<div class="mt35 mod_hot_rank clearfix">.*?<ul>.*?<a.*?>(.*?)</a>', re.S)
results =re.findall(pattern, res)
print(results)
for row in results:
    print(row.strip())


# 获取url接口
comment_url = 'https://news.163.com/'
def get_load():
    resp = requests.get(comment_url)
    html_content = resp.text
    # 获取 xpath
    pattern = '//div[@class="mt35 mod_hot_rank clearfix"]/ul/li/a/text()'
    tree = etree.HTML(html_content)
    album_name = tree.xpath(pattern)
    # 输出结果
    print(album_name)

if __name__ == '__main__':
    album_name =get_load()




