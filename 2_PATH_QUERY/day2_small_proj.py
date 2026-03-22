"""
objectvie : make a small board using POST,GET,DELETE,PUT and pydantic

"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

posts = {}
post_id = 0
app = FastAPI()

# data model
class Post(BaseModel):
    title : str
    content : str
    author : str


@app.post("/posts")
def create_post(post:Post):
    global post_id
    post_data = post.model_dump() # conver json to dic
    post_id += 1
    posts[post_id] = post_data
    return{"message": "stored",
           "length" : len(posts)}

# author fliter, skip, limit
@app.get("/posts")
def get_all(
    author : Optional[str] = Query(None, description = "Fliter by author"),
    skip : int = Query(0,ge=0, description="Number of posts to skip"),
    limit : int = Query(10, gt = 0, description=" Maximum number of posts to return")):

    filtered_posts = [
        {"id": k, **v} for k,v in posts.items()
        if author is None or v["author"] == author
    ]
    return {
        "total" : len(filtered_posts),
        "posts" : filtered_posts[skip : skip + limit]
    }


@app.get("/posts/{id}")
def get_select(id : int):
    if id not in posts.keys():
        raise HTTPException(404,detail="current id is not available")
    return {"id" : id,
            "data" : posts[id]}

@app.put("/posts/{id}")
def edit_post(id : int, post : Post) :
    if id not in posts.keys():
        raise HTTPException(404,detail = "current id is not available")
    posts[id] = post.model_dump()
    return{"message" : "edited", "id" : id}

@app.delete("/posts/{id}")
def delete_data(id : int):
    global post_id,posts
    if id not in posts.keys():
        raise HTTPException(404,detail = "current id is not available")
    posts.pop(id)
    temp_posts = {}
    for i,(_,v) in enumerate(posts.items(), start=1) :
        temp_posts[i] = v
    posts = temp_posts
    post_id = len(posts)
    return{"message" : "success delete", 
           "total" : len(posts)}

