'''
in terminal
uvicorn main:app --reload
main:app -> file:variable
--reload -> if code is edited, server automatically restart


'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # decorator -> if it has "get" request with "/", do below function 
def root():
    return {"message" : "Hello FastAPI"} # dictionary type should be converted automatically to JSON