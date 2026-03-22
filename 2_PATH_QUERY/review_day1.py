from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel


app = FastAPI()

class PostModel(BaseModel):
    name : str
    address : str
    age : str

posts= {}
post_id = 0

@app.post("/posts")
def create_post(post : PostModel):
    global post_id
    post_data = post.model_dump()
    post_id += 1
    posts[post_id] = post_data
    return {"message":"stored",
            "id": post_id}

@app.get("/posts")
def get_all():
    return {"len" : len(posts),
            "posts" : posts}

@app.get("/posts/{id}")
def get_one(id : int) :
    if id not in posts :
        raise HTTPException(status_code=404, detail = "Post not found")
    return {
        "posts" : posts[id]
    }
