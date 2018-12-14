# urllib代理示例
# 为了防止同一个ip频繁访问服务器被封锁，需要不断变化ip通过别人的电脑代理访问服务器。

"""
从哪找代理ip？
ip代理平台：http://www.xicidaili.com/nn/
免费的不太稳定有些可用。付费的稳定
2.网友搜集爬取的ip代理池
"""


import urllib.request
import random

# proxies = [
#     {'http': 'http://124.231.50.56:8118'},
#     {'http':'http://124.231.50.56:8118'},
#     {'http':'http://124.231.50.56:8118'},
#     {'http':'http://124.231.50.56:8118'},
#     {'http':'http://124.231.50.56:8118'}
#
# ]
#proxy = random.choice(proxies)


# 设置代理操作器
proxy = urllib.request.ProxyHandler({'http': 'http://124.231.50.56:8118'})
# 构建新的请求器，覆盖默认opener
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
response = urllib.request.urlopen('http://www.baidu.com/s?wd=ip')
html_content = response.read().decode('utf-8')
print(html_content)

"""
可能出现的错误：
1.长时间未响应：urllib.error.URLError:<urlopen error[WinError 10060]由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接失败。>
2.对方服务器拒绝连接。connectionResetError远程主机关闭了一个现有连接。解决，换一个购买服务器
"""

"""

"""