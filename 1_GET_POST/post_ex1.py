"""
Get vs Post
common : both are reqeust to server

difference :
Get : retrieve data -> please give me this data
Post : generate data -> plese store this data
"""
from fastapi import FastAPI

app = FastAPI()

@app.post("/user")
def create_user(name : str, age : int):
    return{
        "name" : name,
        "age" : age
    }