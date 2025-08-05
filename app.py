from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/eat")
async def read_root():

    return {"Hello": "World"}   
