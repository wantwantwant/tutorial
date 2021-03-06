import pymongo

# 连接数据库
client = pymongo.MongoClient('127.0.0.1',27017)
print(client)
# 切换数据库，如果数据库不存在新建
db = client.test
print(db.name)
# 创建collection集合（相当于mysql中table表）
db.my_collection
print(db.my_collection)
# 插入数据
db.my_collection.insert_one({"x": 10})
db.my_collection.insert_one({"x": 8})
db.my_collection.insert_one({"x": 11})
# 查找一条数据
result1 = db.my_collection.find_one()
print(result1)

# 查找一个集合中所有数据
print('-'*50)
result2 = db.my_collection.find()
for item in result2:
    print(item)
    