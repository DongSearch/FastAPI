from fastapi import FastAPI

app = FastAPI()

posts = {
    1: {"title": "Hello", "content": "first one"},
    2: {"title": "FastAPI", "content": "Path parameter practice"}
}

@app.get("/posts/{post_id}")
def read_post(post_id : int):
    return {"post_id" : post_id, "data" : posts.get(post_id,"Not found")}