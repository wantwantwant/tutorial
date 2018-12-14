import urllib.request
import urllib.parse
import json


# http://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=北京&output=json&ak=您的ak //GET请求
origin_args = {'query': 'ATM机', 'region': '郑州', 'output': 'json','ak': 'YWej2IOY2jdkxwo3cteBdwIsbY26h0lv'}
b64_args = urllib.parse.urlencode(origin_args)
print(b64_args)
# 拼url，请求
base_url = 'http://api.map.baidu.com/place/v2/search'
url = base_url + '?' + b64_args
print('拼好的url', url)
resp = urllib.request.urlopen(url)
content_json = resp.read().decode()
print(content_json)
# json请求
content_obj = json.loads(content_json)
print(content_obj)
results = content_obj['results']
for row in results:
    print(row['name'], row['address'])
