from ..schemas.peliculas import *
from ..config.db import *

from fastapi import APIRouter

pelis = APIRouter()

    #Mostrar Peliculas
def CargarPeliculas():
    peliculas = []
    for pel in Peliculas.select().dicts():
        peliculas.append(pel)
    return peliculas

@pelis.get("/peliculas/", tags=["Peliculas"])
def Lista_Peliculas():
    tmp = CargarPeliculas()
    return tmp

    #Insertar Peliculas
def GuardarPeliculas(obj:peliculas):
    Pel = Peliculas
    Pel.Titulo = obj.Titulo
    Pel.Fecha = obj.Fecha
    Pel.Comentario = obj.Comentario
    Pel.save()

@pelis.post("/peliculas/", tags=["Peliculas"])
def Agregar_Peliculas(Pel: peliculas):
    GuardarPeliculas(Pel)
    return {"Mensaje": "Se ha agregado la pelicula"}

    #Modificar Peliculas
def ActualizarPeliculas(obj:peliculas, titulo: str):
    Pel = Peliculas.get(Peliculas.Titulo == titulo)
    Pel.Titulo = obj.Titulo
    Pel.Fecha = obj.Fecha
    Pel.Comentario = obj.Comentario
    Pel.save()

@pelis.put("/peliculas/{codigo}", tags=["Peliculas"])
def Modificar_Pelicula(Pel: peliculas, titulo: str):
    ActualizarPeliculas(Pel, titulo= titulo)
    return {"Mensaje": "Se ha modificado la pelicula"}

    #Eliminar Peliculas
def EliminarPeliculas(titulo: str):
    Pel = Peliculas.delete().where(Peliculas.Titulo == titulo)
    Pel.execute()

@pelis.delete("/peliculas/{codigo}", tags=["Peliculas"])
def Eliminar_Pelicula(titulo: str):
    EliminarPeliculas(titulo)
    return {"Mensaje": "Se ha eliminado la pelicula"}
