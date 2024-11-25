import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

collections = mydb['Flygplan']

for flygplan in collections.find():
    print('*'*20)
    for key, val in flygplan.items():
        print(key, val)
    print('*'*20)

# print(collections.find_one({'_id':'674433ca9fb9406f3d5ebd32'}))