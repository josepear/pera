## Libraries
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from uvicorn import run as apprun
import os
from contextlib import asynccontextmanager

## Internal
from middlewares.error_handler import ErrorHandler
from routers.auth import auth_router
from config.database import init_db

## Iniciar app
app = FastAPI()
app.title = "Pera"
app.version = "0.0.0a"

@app.on_event("startup")
def on_startup():
    init_db()

## Middlewares
app.add_middleware(ErrorHandler)

## Routers
app.include_router(auth_router)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Pera</h1><h4>Pera forma parte del sistema Gabinet.</h4><p>Pera está desarrollado por <a href="https://damndog.tech" target="blank">Damn Dog Tech</a></p>')

if __name__ == '__main__':
    port = int(os.getenv("PORT"))
    reload = bool(os.getenv("RELOAD"))
    host = os.getenv("HOST")
    apprun("main:app",host=host, port=port, reload=reload)