from fastapi import FastAPI

from src.summarizing.router import router

app = FastAPI()
#Connect the summarize router to app
app.include_router(router)


@app.get("/")
async def root():
    return {"AiPickles": "Hello from Yaroslav Biziuk!!!"}
