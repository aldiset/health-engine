from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/detail")
async def detail():
    return JSONResponse(content={}, status_code=status.HTTP_200_OK)

@router.get("/prediction")
async def prediction():
    return JSONResponse(content={}, status_code=status.HTTP_200_OK)

@router.get("/prevention")
async def prevention():
    return JSONResponse(content={}, status_code=status.HTTP_200_OK)