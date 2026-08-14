# from fastapi import FastAPI,UploadFile,File
# api=FastAPI()
# from helper import predict_damage
# @api.post("/predicted-damage")
# async def predicted_damage(file:UploadFile=File(...)):
#     image_bytes=await file.read()
#     prediction=predict_damage(image_bytes)
#     return {"prediction": prediction}

