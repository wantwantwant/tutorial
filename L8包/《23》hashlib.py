# 哈希 hash
# hash: 概括摘要加密算法，一般的加密，比如a-z对应的数字1-26，abc的密文位器123，abcde的密文位12345.而hash的密文是，不管1kb的txt文件还是几个G得，最终都会生成一哥固定长度的字符串。

#常用加密算法：md5  shal28 sha256
# 优点： 文件轻度修改


"""
场景：
1.校验文件，保证文件被第三方修改。确保下载文件没加入光告或恶意程序
2.校验接口参数。api平台app_key和params生成sign签名，如果传书过程中有被误认为是有误或被中间人截取请求修改，那么签名会不匹配，服务器检测到丢弃。
3.字典，hash表，散列表。hash值作为键名供快速访问。
"""

import hashlib

md5 = hashlib.md5()
md5.update('一些文本，待加密的文件'.encode('utf-8'))
md5.update('追加新的内容生成更新后的摘要'.encode())
# md5.digets()    '\xbdc\x9c'
print(md5.hexdigest())

"""
update() 比较大的文件如视频可以分为多块，多次调用update()。
参数为二进制，待摘要信息是字符串的话先编码。
hex digest 生成十六进制摘要字符串
"""

"""
攻击：穷举，对撞
hsah加密并不是绝对安全
有些人
admin 213221cd2ec432121scds32437csx3
password 75aba38979aa8a665cf0f2dacddcb82c
123456
有攻击者根据弱密码字典(10万个弱密码)通过代码生成md5加密，存入一张数据库表。
如果这个黑客窃取了网站的用户表，即使用户表密码字段存的是密文，跟自己生成的md5做对比，如果对上即知道用户明文密码，冒充用户登录窃取信息钱财。所以密码不建议起的太简单。
"""

# 解决方案：加额外的字符串混淆，俗称加盐salt
salt = 'abc'
md5 = hashlib.md5()
md5.update(('password'+ salt).encode('utf-8'))
print('md5'+ '$'+salt +'$' + md5.hexdigest())
# md5$abc$8223fe8dc0533c6ebbb717e7fda2833c
"""
加盐后，黑客想要穷举攻击，需要每个弱密码加盐再生成字符串，10万个弱密码，加盐前只需要一张10w行数据的表，加盐后每一个盐需要1*10w行，10w密码需要10w+10w行。每个用户注册随机生成一个盐，穷举成本大大提高，黑客放弃攻击。
"""

# 增加安全性  方式二：多次加密 两三次后已经比较安全。
md5 = hashlib.md5()
md5.update('password'.encode('utf-8'))
str1 = md5.hexdigest()
md5 = hashlib.md5()
md5.update(str1.encode('utf-8'))
str2 = md5.hexdigest()
md5 = hashlib.md5()
md5.update(str2.encode('utf-8'))
str3 = md5.hexdigest()
print(str3)