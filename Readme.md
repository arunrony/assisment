**Q1. Write a Code to add Mailing feature in the flask application.**
##### How to run App and send mail
Step -1 : First you need to open project directory
```shell
cd question_1
```
Step -2 : Activates the virutal environment required for the project dependency isolation.
```shell 
 source venv/bin/activate or .\venv\Scripts\activate
```
Step -3 : Installs libraries and dependencies listed in ```requirements.txt``` in active environment..
```python 
 pip install -r requirements.txt
```
Step -4 : Starts the app in development mode. Open http://localhost:5000 to view it in browser..
```python 
 python app.py
```
**Now app is ready to send mail** 

Step -5 : change email recipients E-mail Id in file ```app.py```
```shell 
 ./routes/app.py
```
Step -6 : now Open [http:localhost:5000](http://localhost:5000) it will send an email to recipients email 

Step -7 : check recipients maill box you will be an emaill from
```emaill
me@arunbamniya.com
```
###### NOTE: please check spam box if you did not found mail in mailbox 
----
**Q2. What is openCV ?**

[OpenCV](https://opencv.org/)  ‘Open Source Computer Vision Library’ is an open-source library that includes several hundreds of computer vision algorithms. Using OpenCV, you could pretty much do every Computer Vision task that could ever be imagined

**According to Wikipedia**

Computer vision is an [interdisciplinary scientific field](https://en.wikipedia.org/wiki/Interdisciplinarity) that deals with how computers can be made to gain high-level understanding from [digital images](https://en.wikipedia.org/wiki/Digital_image) or [videos](https://en.wikipedia.org/wiki/Video). From the perspective of [engineering](https://en.wikipedia.org/wiki/Engineering), it seeks to automate tasks that the [human visual system](https://en.wikipedia.org/wiki/Human_visual_system) can do.

In Simple words Computer vision is a field of deep learning that allows the machine to identify, process images just like humans do. In terms of parsing images humans perform extremely well but when it comes to machines detecting objects involves multiple and complex steps, including feature extraction (edges detection, shapes, etc), feature classification, etc.

**More about open CV**

OpenCV contains implementations of more than 2500 algorithms! It is freely available for commercial as well as academic purposes. The library has interfaces for multiple languages, including Python, Java, and C++.

Applications:

##### **OpenCV’s** application areas include:
- 2D and 3D feature toolkits
- Egomotion estimation
- Facial recognition system
- Gesture recognition
- Human–computer interaction (HCI)
- Mobile robotics
- Motion understanding
- And Many More

OpenCV gives access to more than 2,500 state-of-the-art and classic algorithms. By using this library, users can perform various tasks like removing red eyes, extracting 3D models of objects, following eye movements, etc.

----
**Q3. What is Pandas and Write down a code to join two join data frames.**

Pandas is an open-source library that is built on top of NumPy library. It is a Python package that offers various data structures and operations for manipulating numerical data and time series. It is mainly popular for importing and analyzing data much easier. Pandas is fast and it has high-performance & productivity for users.
##### Adavantage of Pandas
- Fast and efficient for manipulating and analyzing data.
- Data from different file objects can be loaded.
- Easy handling of missing data (represented as NaN) in floating point as well as non-floating point data.
- Size mutability: columns can be inserted and deleted from Data Frame and higher dimensional objects.
- Data set merging and joining.
- Flexible reshaping and pivoting of data sets.
- Provides time-series functionality.
- Powerful group by functionality for performing split-apply-combine operations on data sets.
### Code to join two dataframe
To join data frames we have to first create two dataframes then we will concat or we can say we will join those two data frames
##### here is dataframe 1
```python
   In [1]: df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"], }, index=[0, 1, 2, 3], )
```
##### here is dataframe 2
```python
  In [2]: df2 = pd.DataFrame( {
    "A": ["A4", "A5", "A6", "A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"],
    "D": ["D4", "D5", "D6", "D7"],  }, index=[4, 5, 6, 7],)
```
##### here is how you join our Dataframes

```python
In [3]: frames = [df1, df2]
In [4]: result = pd.concat(frames)
```
----
**Q4. Write a Code to add Establish Connection with MongoDB**

```python
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
    print("Congrats User Succesfully inserted " , data)

# deleting single value on collection
def delete_user(query, collection):
    collection.delete_one(query)
    print("Congrats User Succesfully deleted " , query )

# updating single value n the collection
def update_user(query, collection, data_to_update):
    collection.update_one(query, data_to_update)
    print("Congrats User Succesfully updated " , query , "To" , data_to_update )


# main function 
def main():
    database = getDatabase()
    collection = database["user_collection"]
    # insert_user(data= {"_id": 100, "user_name": "Sushil"} , collection=collection)
    # update_user(query={"_id": 100}, collection=collection , data_to_update= {"$set" : {"user_name" : "Gopal Meena"}} )
    # delete_user(query = {"_id": 100} , collection=collection)

# calling main function
if __name__ == "__main__":
    main()

```
##### How to Run Above code
- Uncomment First Line and Run Code It will add a new user to the database
- Uncomment Second Line and Run Code It will Update the user that we have added on the first run to the database
- Uncomment Third Line and Run Code It will Delete the user that we have added on the first run to the database
###### NOTE:- we are using pymongo for establishing connection to the database so make sure to install library using below command
#
```python
$ python3 -m pip install pymongo
```
----
**Q5. Simple post api in python using django framwork**
##### Tasks
- Takes name , date of birth and country as input
- saves information as excel file and as well as to the database also
- Returns JSON response
```
if -> success {"status" :"successfull"}
else->  {"status" :"failed"}
```
##### How to run App
Step -1 : First you need to open project directory
```shell
cd question_5
```
Step -2 : Activates the virutal environment required for the project dependency isolation.
```shell 
 source venv/bin/activate or .\venv\Scripts\activate
```
Step -3 : Installs libraries and dependencies listed in ```requirements.txt``` in active environment..
```python 
 pip install -r requirements.txt
```
Step -4 : Django python manage.py makemigrations command
```python 
 python manage.py makemigrations

```
Step -5 : Django python manage.py migrate command
```python 
 python manage.py migrate
```
Step -6 : Django python Runserver command
```python 
 python manage.py runserver
```
**Now app is Running on port no. 8000** 

Step -6 : now Open [http:localhost:8000](http://localhost:8000)

###### NOTE: Now Follow Below Instructions
#### How to create User
###### Example request:
- **POST** [localhost:8000/api/user_create](http://localhost:8000/api/user_create)
- **Content-Type:** application/json

Example data for content area
```json
{"name": "arun", "dob": "2012-02-12", "country": "India"}
```
Example Response will be

```json
{"status": "successfull"}
```
###### NOTE: An excel file named as sample.xlsx will be found in the root directory of the project where all the data is being append.
#
#### How GET User(s) List
###### Example request:
- **GET** [localhost:8000/api/user](http://localhost:8000/api/user)
- **Content-Type:** application/json

Example Response will be

```json
[
    {
      "id" : 1,
      "name" : "users_name",
      "dob" : "01-01-1979",
      "country" : "USA"
    },
    {
       "id" : 2,
       "name" : "Arun",
       "dob" : "01-01-1979",
       "country" : "UK"
    }
]
```
#
#### How to GET any specific user via id
###### Example request:
- **GET** [localhost:8000/api/user/replace_with_id](http://localhost:8000/api/user/2)
- **Content-Type:** application/json

Example Response will be

```json
{
   "id" : 1,
   "name" : "users_name",
   "dob" : "01-01-1979",
   "country" : "USA"
}
```
