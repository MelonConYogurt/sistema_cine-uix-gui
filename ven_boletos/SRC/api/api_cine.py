from fastapi import FastAPI, HTTPException
from typing import List
from SRC.api.modelos import *
from SRC.main.data_base_cine import *

app = FastAPI()

# ---Conexion de la base de datos------

base_datos = conexion_base_datos()

@app.get("/salas/")
async def obtener_salas():
    lista_salas = base_datos.buscar_salas()
    if lista_salas:
        return lista_salas
    else:
        raise HTTPException(status_code=404, detail="No se encontraron salas")

@app.post("/asientos/")
async def agregar_asientos(asiento: model_asiento):
    nuevo_asiento = base_datos.anadir_asientos(
        nombre_sala = asiento.sala,
        numero_asiento= asiento.numero_asiento,
        seccion_asiento= asiento.seccion_asiento,
        fecha= asiento.fecha_asiento
    )
    if nuevo_asiento:
        return asiento
    else:
        raise HTTPException(status_code=400, detail="No se pudo añadir el asiento")

if __name__ == "__main__":
    pass