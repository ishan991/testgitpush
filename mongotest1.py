import pymongo
client = pymongo.MongoClient("mongodb+srv://ishan991:ishan@ishan.7u6ck.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)      # if it print without error it means it has correct connection

d= {
    "name" : "ishan",
    "email" : "ishandwivedi100@gmail.com",
    "surname" : "dwivedi"
}
d= {
    "name" : "ishan",
    "email" : "ishandwivedi100@gmail.com",
    "surname" : "dwivedi"
}
d= {
    "name" : "ishan",
    "email" : "ishandwivedi100@gmail.com",
    "surname" : "dwivedi"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
