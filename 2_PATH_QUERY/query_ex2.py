from fastapi import FastAPI

app = FastAPI()

posts = {
    1: {"title": "Hello", "content": "첫 글입니다"},
    2: {"title": "FastAPI", "content": "Path parameter 연습"}
}

@app.get("/posts/")
def read_posts(author: str = None, limit : int = 10):
    return {"author" : author, "limit" : limit}