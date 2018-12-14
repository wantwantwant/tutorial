import urllib.request
import urllib.parse
import json


# http://api.map.baidu.com/place/v2/suggestion?query=天安门&region=北京&city_limit=true&output=json&ak=你的ak //GET请求
origin_args = {'query': '清华', 'region': '北京', 'city_limit': 'true', 'output': 'json', 'ak': 'YWej2IOY2jdkxwo3cteBdwIsbY26h0lv'}
b64_args = urllib.parse.urlencode(origin_args)
print(b64_args)
# 拼url
base_url = 'http://api.map.baidu.com/place/v2/suggestion'
url = base_url + '?'+ b64_args
print('拼好的url', url)
resp = urllib.request.urlopen(url)
content_json = resp.read().decode()
print(content_json)
# json请求
content_obj = json.loads(content_json)
print(content_obj)
over = content_obj['result']
for row in over:
    print(row['name'], row['city'])