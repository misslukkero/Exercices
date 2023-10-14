from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class comune (BaseModel):
    id: int
    nombre: str
    telefono: int
    email: str
    puntaje: Optional [int]

@app.get ("/")
def index ():
    return ("Hola futuros citadinos Italianos")

@app.get ("/comune/{id}")
def mostrar_comune(id: int):
    return {"data", id}

@app.post ("/comune/")
def insertar_comune(comune: comune):
    return {"message" , "Comune {comune.nombre} insertada en la base de datos"}

@app.delete ("/comune/")
def eliminar_comune (comune: comune):
    return {"message" , "Comune {comune.nombre} eliminada de la base de datos}"}

@app.put ("/comune/")
def actualizar_comune(comune: comune):
    return {"message" , "Comune {comune.nombre} actualizada en la base de datos"}

