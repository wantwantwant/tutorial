# （爬虫、django）
# 需求，给你一个网站一个页面的源代码，要求把网址都选出来，返回列表。''.find()可以但麻烦。如果需求复杂find不能胜任。
# 正则：re regex。专业做字符串查找筛选。比''.find()强大的多。有自己专用的语法。优点：功能最为强大，缺点是学习曲线陡峭。
# 场景：爬虫、网页解析、匹配、flask django框架的路由就是基于正则的。
# regex 三方包，功能比内置的re包更加强大。
# 前缀r，raw原始字符串，运行中不需要处理转义字符。 print('abc\nabc')             print(r'abc\nabc')


import re

# find()  简单但功能有限不方便
html = r'<html><body><h1>hello world</h1></body></html>'
start_index = html.find('<h1>')
end_index = html.find('</h1>')
print(html[start_index: end_index+1])

# 1> 匹配固定字符串一次
key = r'bchsbacbdchbwshbACHBHCWWDwdqd'
pattern1 = re.compile(r'CWWD')
matcher1 = re.search(pattern1, key)
print(matcher1)
print(matcher1[0])

# compile (正则规则) 返回包含规则的匹配器对象
# re.search(匹配器对象，待查找字符串)

# 2> 任意字符串          .匹配任意字符 +主要修饰前面的匹配规则重复一次或多次  .+匹配一个或多个任意字符。
key = r'<h1>hello world</h1>'
pattern2 = p2 = r'<h1>.+</h1>'
matcher2 = re.search(pattern2, key)
print(matcher2[0])


# 3> 匹配 点 加号, 转义\  .匹配任意字符， +前面的字符一次或多次
key3 = r'738272@qq.com'
p3 = re.compile(r'.+@qq\.com')        # 匹配用户输入是否qq邮箱。 .+不太准确
m3 = re.search(p3, key3)
print(m3[0])

# 4> *前面的字符出现0次或多次
key4 = r'http://www.baidu.com https://www.baidu.com'
p4 = re.compile(r'https*://')
m4 = re.search(p4, key4)
matcher4 = p4.findall(key4)
print(matcher4)

# 匹配器 findall（带匹配字符串） 返回列表

# 5> [aA]匹配一个字符 中括号里任意一个字符符合就算匹配到
key = r'selectSELECTselECT'  # sql大小写不敏感
p1 = re.compile(r'[se][SE][Se]')
patter1 = re.compile(p1)
print(patter1.findall(key))

# 6> 排除
key6 = r'mat cat hat pat'
p6 = re.compile(r'[^p]at')
print(p6.findall(key6))

# 7> 如果符合条件默认匹配尽可能多的字符。 贪婪匹配
key7 = r'132322@163.com.cn'  # 需求 截取出132322
p7 = re.compile(r'.+@.+\.')
print(p7.findall(key7))

# 8> 惰性匹配  +?  符合任意多字符的情况下  字符最少的
p8 = re.compile(r'.+@.+?\.')
print(p8.findall(key7))

# 9> 固定次数
key9 = r'saas and sas and saaas'
p9 = re.compile(r'sa{1,2}s')
print(p9.findall(key9))

# 10> 匹配换行后的内容  re.S
key10 = r"""
aaaaahelloggg
bbb
cc
world
"""
p10= re.compile(r'hello.*?world', re.S)
print(p10.findall(key10))

# 11> 分组  (子正则式)  返回元组，每一项对应每一个子正则式匹配的结果
key11 = r"""hello小明worldaaa"""
p11 = re.compile(r'hello(.*?)world(.*?)')
print(p11.findall(key11))

# 作业： 课下百度re包其他用法。re.match()  re.findall()  re.finditer()