import uvicorn
from fastapi import FastAPI
from app.config.config import TITLE, DESCRIPTION
from app.router import chat, health, room, test

app = FastAPI(
        debug=True, 
        title=TITLE,
        description=DESCRIPTION
    )

@app.get("/", tags=["Index"])
async def index():
    return "Welcome in Health Engine"

app.include_router(chat, prefix="/chat", tags=["Chat"])
app.include_router(room, prefix="/room", tags=["Room"])
app.include_router(health, prefix="/health", tags=["Health"])
app.include_router(test, prefix="/test", tags=["Test"])

if __name__ == "__main__":
    uvicorn.run(app)