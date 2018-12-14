# python字典和通用结构json相互转换

import json

student_list = [
    {'no': 1, 'name': '小明', 'age': 13},
    {'no': 2, 'name': '小花', 'age': 15},
    {'no': 3, 'name': '阿坤', 'age': 18}
]

student_json = """
{
     "student_list": [
          {"no": 1, "name": "小明", "age": 13},
          {"no": 2, "name": "小花", "age":15},
          {"no": 3, "name": "阿坤", "age": 18}
     ],
     "school_name": "香奈儿",
     "address": "巴黎"
}
"""

# 对象转json
stu_json = json.dumps(student_list, indent=4)
print(type(stu_json), stu_json)

"""
json.dumps（数据对象）  返回json格式字符串。
形如\u5c0f是中文的unicode编码。计算机传输的本质是二进制信息。
"""

# json转对象
stu_obj = json.loads(student_json)
print(stu_obj)
for stu in stu_obj['student_list']:
    print(f'学生姓名{stu["name"]}')

# json.dumps()  json.load() 这两个方法的参数是文件
# dumps()   loads() 参数是变量
with open('《7》天气接口返回数据.json', encoding='utf-8') as file:
    weather_obj = json.load(file)
    print(weather_obj)


# 面试题：
