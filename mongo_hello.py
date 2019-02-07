# instalando o client pip install pymongo
# user  pass user31
#  python -m pip install pymongo[srv]
#  https://cloud.mongodb.com/user#/atlas/login
# url kRrjnv6!BXnQw-A

from pymongo import MongoClient


client = MongoClient("mongodb+srv://user:user31@cluster0-fc9gz.mongodb.net/test?retryWrites=true")

print(client.list_database_names())

#print(client.list_collection_names())



