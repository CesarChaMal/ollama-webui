import os
from fastapi import APIRouter
import httpx
from config import OLLAMA_API_BASE_URL, OLLAMA_HOST, OLLAMA_WEBAPI_PREFIX
from fastapi import APIRouter
import httpx

router = APIRouter()

print(f"✅ OLLAMA_API_BASE_URL = {OLLAMA_API_BASE_URL}")
if not OLLAMA_API_BASE_URL.startswith("http"):
    raise ValueError(f"OLLAMA_API_BASE_URL must start with 'http', but got: {OLLAMA_API_BASE_URL}")

print(f"✅ OLLAMA_HOST = {OLLAMA_HOST}")
if not OLLAMA_HOST.startswith("http"):
    raise ValueError(f"OLLAMA_HOST must start with 'http', but got: {OLLAMA_HOST}")

print(f"✅ OLLAMA_WEBAPI_PREFIX = {OLLAMA_WEBAPI_PREFIX}")
if not OLLAMA_WEBAPI_PREFIX.startswith("/"):
    raise ValueError(f"OLLAMA_WEBAPI_PREFIX must start with '/', but got: {OLLAMA_WEBAPI_PREFIX}")

@router.get("/url")
async def get_ollama_api_url():
    return {"url": OLLAMA_API_BASE_URL}

@router.get("/version")
async def get_ollama_version():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{OLLAMA_API_BASE_URL}/version")
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        return {"error": f"Connection error to Ollama API: {str(e)}"}
    except httpx.HTTPStatusError as e:
        return {"error": f"Ollama API returned error: {e.response.text}"}

@router.get("/tags")
async def get_ollama_tags():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{OLLAMA_API_BASE_URL}/tags")
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        return {"error": f"Connection error to Ollama API: {str(e)}"}
    except httpx.HTTPStatusError as e:
        return {"error": f"Ollama API returned error: {e.response.text}"}
