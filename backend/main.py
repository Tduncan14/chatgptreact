from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    print('this is treek')
    return {"message": "Hello World"}