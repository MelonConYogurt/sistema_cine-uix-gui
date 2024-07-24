from fastapi import FastAPI, HTTPException
from typing import List
from SRC.api.modelos import *
from SRC.main.data_base_cine import *

app = FastAPI()

# ---Conexion de la base de datos------
base_datos = conexion_base_datos()


# @app.get("//")
# async def obtener_salas():
#     lista_salas = base_datos.buscar_salas()
#     if lista_salas:
#         return lista_salas
#     else:
#         raise HTTPException(status_code=404, detail="No se encontraron salas")

@app.post("/crear/asientos/")
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

@app.post("/crear/salas/")
async def agregar_salas(sala: model_sala):
    try:
        nueva_sala = base_datos.anadir_sala(
            nombre_sala = sala.nombre_sala,
            capacidad_sala = sala.capacidad_sala,
            estado_sala = sala.estado_sala 
        )
        if nueva_sala:
            return sala
        else:
            raise HTTPException(status_code=400, detail="No se pudo añadir el asiento")
    except Exception as e:
        pass
                
@app.post("/crear/peliculas/")
async def agregar_peliculas(pelicula: model_pelicula):
    nueva_pelicula = base_datos.anadir_pelicula(
        titulo_pelicula = pelicula.titulo_pelicula,
        genero_pelicula = pelicula.genero_pelicula,
        duracion_pelicula = pelicula.duracion_pelicula,
        rating_pelicula = pelicula.rating_pelicula
        )
    if nueva_pelicula:
        return  pelicula
    else:
        raise HTTPException(status_code=400, detail="No se pudo añadir el asiento")
        
    
@app.post("/crear/clientes/")
async def agregar_cliente(cliente: model_clientes):
    nuevo_cliente = base_datos.anadir_cliente(
        nombre_cliente = cliente.nombre_cliente,
        apellido_cliente = cliente.apellido_cliente,
        correo_cliente = cliente.correo_cliente,
        documento = cliente.documento_cliente
        )
    if nuevo_cliente:
        return cliente
    else:
         raise HTTPException(status_code=400, detail="No se pudo añadir el asiento")
        
@app.post("/crear/horarios/")
async def agregar_horarios(horario: model_horarios):
    nuevo_horario = base_datos.anadir_horarios(
        nombre_pelicula = horario.nombre_pelicula,
        nombre_sala = horario.nombre_sala,
        fecha_date = horario.fecha_funcion
    )
    if nuevo_horario:
        return horario
    else:
         raise HTTPException(status_code=400, detail="No se pudo añadir el asiento")

if __name__ == "__main__":
    pass