import uvicorn
from fastapi import FastAPI
from app.config.config import TITLE, DESCRIPTION
from app.router import assesment, checker, analysis

app = FastAPI(
        debug=True, 
        title=TITLE,
        description=DESCRIPTION
    )

@app.get("/", tags=["Index"])
async def index():
    return "Welcome in Health Engine"

app.include_router(assesment)
app.include_router(checker)
app.include_router(analysis)
if __name__ == "__main__":
    uvicorn.run(app)