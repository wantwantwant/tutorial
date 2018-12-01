# base64编码

# 引题：读写图片、视频我们读出二进制。
# 计算机之间交流一般通用格式信息，比如字符串'hello world'。比较老式的服务器由于硬件和软件的限制只支持ascii编码，不支持特殊符号，直接传输字节信息可能会出错。

# 图片（jpg编码） → 二进制（base64编码） → 处理后字符串 ，
# 处理后的字符串适合在网络中传播。

# base64编码:一种简单的加密方法。主要作用是轻度加密和兼容老服务器。会把原信息转换成由大小写字母和常见字符组成的新的字符串。
# 场景：
#    1.网址。网址含有中文，比如http://www.baidu.com/新闻、国内，网址复制粘贴出来后形如http://8E%E8%AE%A4%E8%/,这就是经过base64转码后的结果，服务器识别网址时就不会出错了。
#   2.传图片。不传字节而传通用的字符串。
#   3.简单加密。比如v2ex论坛上自爆微信号的时候发出来是经过base64编码后的内容。

# 参考（了解） 百度百科https://baike.baidu.com/item/base64/8545775?fr=aladdin

import base64
#content = base64.b64encode('我的电话是15093315773'.encode())
with open('6img.jpg','rb') as f:
    content_bytes = f.read()
    content_b64 = base64.b64encode(content_bytes)
print(content_b64)

"""
b64encode(待转换的字母)
"""
