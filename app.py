from fastapi import FastAPI
from starlette.responses import  RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from .routes.peliculas import pelis

app = FastAPI(
    title="Proyecto Final",
    description="Moises Nuñez | 2020-10457"
)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

app.include_router(pelis)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)