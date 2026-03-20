from fastapi import FastAPI

app = FastAPI()

posts = [] # storage

@app.post("/posts")
def store(title : str, content : str, author : str):
    post = {
        "title" : title,
        "content" : content,
        "author" : author
    }
    posts.append(post)
    return {"message" : "created"}
