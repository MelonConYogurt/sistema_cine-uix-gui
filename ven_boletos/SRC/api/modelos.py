from pydantic import BaseModel
from datetime import datetime


class model_asiento(BaseModel):
    sala: str
    numero_asiento: int
    seccion_asiento: str
    fecha_asiento: datetime

class model_sala(BaseModel):
    nombre_sala: str
    capacidad_sala: int
    estado_sala: int
    
class model_pelicula(BaseModel):
    titulo_pelicula: str
    genero_pelicula: str
    duracion_pelicula: int 
    rating_pelicula: int

class model_clientes(BaseModel):
    nombre_cliente: str
    apellido_cliente: str
    correo_cliente: str
    documento_cliente: str

class model_horarios(BaseModel):
    nombre_pelicula: str
    nombre_sala: str
    fecha_funcion: any
    
    
    
    
if __name__ == "__main__":
    pass