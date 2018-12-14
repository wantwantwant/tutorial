# User-Agent伪造
# User-Agent:request_heads请求头中的一个字段，包含操作系统和浏览器信息。
# 如果来自同一个UserAgent的请求过于频繁，服务器有可能封掉。所以我们伪造User_Agent信息。

import random

def get_random_user_agent():
    user_agent_list = [
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        ]
    return random.choice(user_agent_list)

# print(get_random_user_agent())
user_agent = get_random_user_agent()

# 后续操作，加入请求头请求
# import urllib.request
# req = urllib.request.Request('https://www.baidu.com', data={'wd': 'python'})
# req.add_header('User_Agent', user_agent)
# resp = urllib.request.urlopen(req)
# print(resp)
# html = resp.read().decode()
# print(html)

from fake_useragent import UserAgent
ua = UserAgent()
print(ua.random)