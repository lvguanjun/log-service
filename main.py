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
LOG_BASE_DIR = os.getenv("LOG_BASE_DIR", "./logs")

if not os.path.exists(LOG_BASE_DIR):
    os.makedirs(LOG_BASE_DIR)


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

    log_file = os.path.join(LOG_BASE_DIR, f"{log.service}.log")

    with open(log_file, "a") as f:
        f.write(log_entry)

    return {"detail": "Log saved."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000)
