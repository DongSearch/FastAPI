from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # generate instance

posts = [] # list to store  data(for temporary use)
post_id = 1 # id for each post

# id should be magaged in server
class Post(BaseModel): #pydantic shape
    title : str
    content : str
    author : str

@app.post("/posts")
def store(post: Post):
    global post_id

    post_data = post.model_dump() # convert Pydantic to Dictionary
    post_data["id"] = post_id # add unique ID
    posts.append(post_data) # add it to list
    post_id += 1
    return{"message" : "created",
           "post": post_data}

@app.get("/posts")
def retrieve_all():
    return {"posts": posts}

@app.get("/posts/{id}")
def retrieve(id: int) :
    for p in posts:
        if p["id"] == id :
            return p
        else :
            return {"error" : "post not found"}