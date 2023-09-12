from sqlalchemy import and_
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, APIRouter, status

from app.engine.engine import ChatGPT
from app.database.object import Object
from app.utils.random_color import random_color
from app.utils.get_json import get_json_from_string
from app.models.models import HealthData, CheckUpHistory, AIResult, PreventionData
from app.schema.health import HealthCreateSchemaBulk, CheckUpCreateSchemaBulk

router = APIRouter()

success_response = {"message": "success", "data": []}
health_object = Object(HealthData)
checkup_object = Object(CheckUpHistory)
airesult_object = Object(AIResult)
prevention_object = Object(PreventionData)


@router.get("/{user_id}/detail")
async def get_user_detail(user_id: str):
    data = []
    health_filters = [and_(HealthData.user_id == user_id)]
    checkup_filters = [and_(CheckUpHistory.user_id == user_id)]

    diseases = await health_object.get_all(*health_filters)
    checkup_history = await checkup_object.get_all(*checkup_filters)

    data.append({"disease": jsonable_encoder(diseases)})
    data.append({"check_up_history": jsonable_encoder(checkup_history)})

    return JSONResponse(content=success_response, status_code=status.HTTP_200_OK)


@router.get("/{user_id}/prediction")
async def get_user_prediction(user_id: str):
    data = []
    health_filters = [and_(HealthData.user_id == user_id)]
    diseases = await health_object.get_all(*health_filters)

    for disease in diseases:
        data.append(f"{disease.title}:{disease.value}")

    chatgpt_prompt = (
        f"Tuliskan Json List yang berisi prediksi penyakit berdasarkan data {data} "
        "Tulisakan ke dalam List Json "
        "[{\"nama_penyakit\":\"value\",\"gejala\":\"value\",\"deskripsi\":\"value\"}]"
    )

    chatgpt = ChatGPT(model="text-davinci-003", prompt=chatgpt_prompt)
    result = await chatgpt.completion()

    if result:
        print(result)
        result_json = get_json_from_string(result)
        if isinstance(result_json, list):
            ai_result = await airesult_object.create({"user_id": user_id, "data": result_json})
            success_response["data"] = {"ai_result_id": ai_result.id, "prediction": ai_result.data}
        else:
            print(result)

    return JSONResponse(content=success_response, status_code=status.HTTP_200_OK)


@router.get("/{ai_result_id}/prevention")
async def get_prevention_by_ai_result(ai_result_id: str):
    ai_result = await airesult_object.get_by_id(ai_result_id)
    
    if not ai_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    diseases_name = [disease.get("nama_penyakit") for disease in ai_result.data]

    chatgpt_prompt = (
        f"Pencegahan penyakit berdasarkan data: {diseases_name}. "
        "Tulisakan ke dalam List Json "
        "[{\"nama_penyakit\":\"value\",\"pencegahan\":[\"value\", \"value\"],\"deskripsi\":\"value\"}]."
    )

    chatgpt = ChatGPT(model="text-davinci-003", prompt=chatgpt_prompt)
    result = await chatgpt.completion()

    if result:
        result_json = get_json_from_string(result)
        if isinstance(result_json, list):
            prevention_data = await prevention_object.create({"ai_result_id": ai_result_id, "data": result_json})
            success_response["data"] = prevention_data.data
        else:
            print("result >> ", result)
    
    return JSONResponse(content=success_response, status_code=status.HTTP_200_OK)


@router.post("/create/bulk")
async def create_health_bulk(datas: HealthCreateSchemaBulk):
    for data in datas.data:
        data_dict = jsonable_encoder(data)
        data_dict["color"] = random_color()
        await health_object.create(data_dict)
    
    return JSONResponse(content=success_response, status_code=status.HTTP_200_OK)


@router.post("/checkup/create/bulk")
async def create_checkup_bulk(datas: CheckUpCreateSchemaBulk):
    for data in datas.data:
        data_dict = jsonable_encoder(data)
        await checkup_object.create(data_dict)
    
    return JSONResponse(content=success_response, status_code=status.HTTP_200_OK)