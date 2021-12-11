from pydantic import BaseModel

class peliculas(BaseModel):
    Titulo: str
    Fecha: str
    Comentario: str