from fastapi import FastAPI,UploadFile,File
api=FastAPI()
from helper import predict_damage
@api.post("/predicted-damage")
async def predicted_damage(file:UploadFile=File(...)):
    image_bytes=await file.read()
    image_path = r"C:\Users\vaisa\Downloads\project damage detection\streamlit-app\screenshots\temp.jpg"
    with open(image_path,'wb') as f:
        f.write(image_bytes)
    prediction=predict_damage(image_path)
    return {"prediction": prediction}

