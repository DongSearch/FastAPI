from fastapi import FastAPI, HTTPException,Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

posts = []
post_id = 0

class Post(BaseModel):
    title : str
    content : str
    author : str
    age : int
    like : int = 0
    view_count : int = 0

class PostUpdate(BaseModel):
    title : Optional[str] = None
    content : Optional[str] = None
    author : Optional[str] = None
    age : Optional[int] = None

@app.post("/post")
def create_post(post : Post):
    global post_id
    post_id +=1
    post_data = post.model_dump()
    post_data["id"] = post_id
    posts.append(post_data)
    return {"message" : "created",
            "data" : post_data}


@app.get("/post")
def get_all(
    author : Optional[str] = Query(None, description= " filtered by author"),
    limit : int = Query(10,gt=0, description = " Maximum num of post"),
    skip : int = Query(0, ge = 0, description= " number of posts to skip"),
    sort : Optional[str] = Query(None),
    order : str = Query("asc")
):
    filtered_post = [
        post for post in posts if author is None or author in post["author"] 
    ]

    if sort :
        if sort not in ["age", "like", "view_count"]:
            raise HTTPException(status_code=400, detail= "Invalid sort field")
        
        reverse = True if order == "desc" else False
        filtered_post = sorted(filtered_post, key = lambda x : x[sort], reverse=reverse)
        

    return {"total" : len(filtered_post),
            "posts" : filtered_post[skip:skip + limit]}

@app.get("/post/{id}")
def get_one(id : int) :
    for post in posts :
        if post["id"] == id :
            post["view_count"] += 1
            return post
    raise HTTPException(status_code=404, detail = " Post not found")

@app.post("/post/{id}/like")
def like_post(id :int):
    for p in posts :
        if p["id"] == id :
            p["like"] += 1
            return {"message" : "liked" , "likes" : p["like"]}
    raise HTTPException(status_code=404, detail = "Post not found")

@app.delete("/post/{id}")
def delete_post(id:int):
    for i, post in enumerate(posts):
        if post["id"] == id :
            posts.pop(i)
            return {"message" : "Deleted"}
    raise HTTPException(status_code=404, detail = " Post not found")

@app.put("/post/{id}")
def edit_post(id : int ,post:Post):
    for i, p in enumerate(posts):
        if p["id"] == id :
            updated  = post.model_dump()
            updated["id"] = id
            # !!! keep like and view_point
            updated["like"] = p["like"]
            updated["view_count"] = p["view_count"]
            
            posts[i] = updated
            return {"message" : "edited", "data": updated}
    raise HTTPException(status_code=404, detail = " Post not found")

@app.patch("/post/{id}")
def edit_part(id : int , post : PostUpdate) :
    for p in posts : 
        if p["id"] == id : 
            update_data = post.model_dump(exclude_unset= True) # ignore the data that user didn't put in

            for k ,v in update_data.items():
                p[k] = v
            return {"message" : "partially updated", "data" : p}
    raise HTTPException(status_code=404, detail = " Post not found")
        
    