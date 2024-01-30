#import sys
#sys.path.append('/content/backend')

import os
import sys

# Get the directory of the current script (main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the base directory of the project (one level up from current_dir)
base_dir = os.path.dirname(current_dir)

# Construct the path to the backend directory
backend_dir = os.path.join(base_dir, 'backend')

# Append the dynamically constructed backend path to sys.path
sys.path.append(backend_dir)


import time

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi import HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException


from apps.ollama.main import app as ollama_app
from apps.openai.main import app as openai_app

from apps.web.main import app as webui_app
from apps.rag.main import app as rag_app

from config import ENV, FRONTEND_BUILD_DIR


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        try:
            return await super().get_response(path, scope)
        except (HTTPException, StarletteHTTPException) as ex:
            if ex.status_code == 404:
                return await super().get_response("index.html", scope)
            else:
                raise ex


app = FastAPI(docs_url="/docs" if ENV == "dev" else None, redoc_url=None)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def check_url(request: Request, call_next):
    start_time = int(time.time())
    response = await call_next(request)
    process_time = int(time.time()) - start_time
    response.headers["X-Process-Time"] = str(process_time)

    return response


app.mount("/api/v1", webui_app)

app.mount("/ollama/api", ollama_app)
app.mount("/openai/api", openai_app)
app.mount("/rag/api/v1", rag_app)


import os

#app.mount("/", SPAStaticFiles(directory="../build", html=True), name="spa-static-files")
#app.mount("/", SPAStaticFiles(directory="/content/build", html=True), name="spa-static-files")

# Construct the path to the build directory
build_dir = os.path.join(base_dir, 'build')

# Use the dynamically constructed path in app.mount
app.mount("/", SPAStaticFiles(directory=build_dir, html=True), name="spa-static-files")

