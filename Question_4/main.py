# PyMongo is a Python distribution containing tools for working with MongoDB
from pymongo import MongoClient


# creating database if doesnt exist
def getDatabase():
    cluster = MongoClient(
        "mongodb+srv://root:root@cluster0.o8ehzeq.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["my_database"]
    return db


# inserting single value on collection
def insert_user(data, collection):
    collection.insert_one(data)
    print("Congrats User Succesfully inserted ", data)


# deleting single value on collection
def delete_user(query, collection):
    collection.delete_one(query)
    print("Congrats User Succesfully deleted ", query)


# updating single value n the collection
def update_user(query, collection, data_to_update):
    collection.update_one(query, data_to_update)
    print("Congrats User Succesfully updated ", query, "To", data_to_update)


# main function
def main():
    database = getDatabase()
    collection = database["user_collection"]
    # insert_user(data= {"_id": 100, "user_name": "Arun"} , collection=collection)
    # update_user(query={"_id": 100}, collection=collection , data_to_update= {"$set" : {"user_name" : "Arun Bamniya"}} )
    # delete_user(query = {"_id": 100} , collection=collection)


# calling main function
if __name__ == "__main__":
    main()
