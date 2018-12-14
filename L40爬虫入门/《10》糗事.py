from urllib import request, parse
import random
import re

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
]

base_url = 'https://www.qiushibaike.com/hot/page/'

def down_load(page):
    req_url = base_url + str(page) + '/'
    headers = {
        'User-Agent': random.choice(user_agent_list)
    }
    req = request.Request(url=req_url, headers=headers)
    resp = request.urlopen(req)
    raw_html = resp.read().decode('utf-8')

    pattern = re.compile(r'<div class="author clearfix">.*?<div class="content">.*?<span>(.*?)</span>', re.S)
    info_list = re.findall(pattern, raw_html)
    for info in info_list:
        print(info)



if __name__ == '__main__':
    for i in range(12):
        print(down_load(i))

