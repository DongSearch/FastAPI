from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message" : "Hello World"}

@app.get("/bye")
def bye():
    return {"message" : "Goodbye"}