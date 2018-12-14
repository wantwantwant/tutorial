import urllib.request
import urllib.parse
import json



#http://api.map.baidu.com/location/ip?ip=xx.xx.xx.xx&ak=你的ak&coor=bd09ll
origin_args = {'ip': '61.135.169.81', 'ak': 'YWej2IOY2jdkxwo3cteBdwIsbY26h0lv', 'coor': 'bd0911'}
b64_args = urllib.parse.urlencode(origin_args)
print(b64_args)
url= 'http://api.map.baidu.com/location/ip' + '?' + b64_args
print(url)
resp = urllib.request.urlopen(url)
content_json = resp.read().decode('utf-8')
print(content_json)
content_obj = json.loads(content_json)
print(content_obj)

