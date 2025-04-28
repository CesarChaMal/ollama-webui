from fastapi import FastAPI, Depends
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from apps.web.routers import (
    auths,
    users,
    chats,
    documents,
    modelfiles,
    prompts,
    configs,
    utils,
    ollama
)
from config import WEBUI_VERSION, WEBUI_AUTH, DEFAULT_MODELS, DEFAULT_PROMPT_SUGGESTIONS, OLLAMA_API_BASE_URL, OLLAMA_HOST, OLLAMA_WEBAPI_PREFIX

app = FastAPI()

origins = ["*"]

app.state.ENABLE_SIGNUP = True
app.state.DEFAULT_MODELS = DEFAULT_MODELS
app.state.DEFAULT_PROMPT_SUGGESTIONS = DEFAULT_PROMPT_SUGGESTIONS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print(f"✅ OLLAMA_WEBAPI_PREFIX = {OLLAMA_WEBAPI_PREFIX}")
if not OLLAMA_WEBAPI_PREFIX.startswith("/"):
    raise ValueError(f"OLLAMA_WEBAPI_PREFIX must start with '/', but got: {OLLAMA_WEBAPI_PREFIX}")


app.include_router(auths.router, prefix="/auths", tags=["auths"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(chats.router, prefix="/chats", tags=["chats"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(modelfiles.router, prefix="/modelfiles", tags=["modelfiles"])
app.include_router(prompts.router, prefix="/prompts", tags=["prompts"])
app.include_router(configs.router, prefix="/configs", tags=["configs"])
app.include_router(utils.router, prefix="/utils", tags=["utils"])
app.include_router(ollama.router, prefix=OLLAMA_WEBAPI_PREFIX, tags=["ollama"])


@app.get("/")
async def get_status():
    return {
        "status": True,
        "version": WEBUI_VERSION,
        "auth": WEBUI_AUTH,
        "default_models": app.state.DEFAULT_MODELS,
        "default_prompt_suggestions": app.state.DEFAULT_PROMPT_SUGGESTIONS,
        "ollama_api_url": OLLAMA_API_BASE_URL
    }
