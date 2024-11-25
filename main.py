import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

collections = mydb['Flygplan']

flygplan1 = {'model':'Airbus 380', 
             'regnummer':'SE-ESR',
             'color':'White',
             'passangers': 34}

flygplan2 = {'model':'Airbus 600', 
             'regnummer':'SE-OPS',
             'color':'Black',
             'passangers': 200}

flygplan3 = {'model':'Airbus 100', 
             'regnummer':'SE-KES',
             'color':'Blue',
             'passangers': 150}


collections.insert_one(flygplan1)

collections.insert_many([flygplan2, flygplan3])

