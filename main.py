#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2024/02/06 13:45:41
@Author  :   lvguanjun
@Desc    :   main.py
"""


import os
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()

load_dotenv()
API_KEY = os.getenv("API_KEY")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))


class Log(BaseModel):
    service: str
    message: str


@app.post("/logs")
async def create_log(log: Log, request: Request):
    if API_KEY:
        api_key = request.headers.get("X-API-KEY")
        if api_key != API_KEY:
            raise HTTPException(status_code=400, detail="Invalid API key")

    timestamp = datetime.now().isoformat()
    log_entry = f"[{timestamp}] [{log.message}]\n"

    log_file = f"{log.service}.log"

    with open(log_file, "a") as f:
        f.write(log_entry)

    return {"detail": "Log saved."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host=HOST, port=PORT)
