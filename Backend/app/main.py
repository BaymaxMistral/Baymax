from typing import List
import uvicorn
from fastapi import BackgroundTasks, FastAPI, HTTPException, Security, status
from fastapi.middleware.cors import CORSMiddleware
from schemas import User_query_model            # model
from model_inference import Process_user_query  # api

app = FastAPI(title="mistral-hackathon-app")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# routes
@app.post("/get_response")
async def get_response(params: User_query_model):
    # \\ call the model here
    obj1 = Process_user_query()
    response = obj1.start_query_process(user_query=params.user_query)
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)




