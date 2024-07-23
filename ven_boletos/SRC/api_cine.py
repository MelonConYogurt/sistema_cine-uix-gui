from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from SRC.data_base_cine import *
from pydantic import BaseModel

# db_conector = base_datos = conexion_base_datos()
# app = FastAPI(
#     title="Api de usuarios",
#     description="Api para el manejo de usuarios en una base de datos.",
#     version="1.0.0",
#     openapi_tags=[
#         {"name": "Usuarios", "description": "Operaciones relacionadas con usuarios en la base de datos."}
#     ],
# )

# # app.include_router(router_secundario)
# # app.include_router(router_terciario)

# app.mount("/photos", StaticFiles(directory="photos"), name="gallery")
# app.mount("/media", StaticFiles(directory="videos"), name="videos_production")

# class UserInfo(BaseModel):
#     id: int
#     nombre: str
#     apellido: str
#     edad: int
#     correo: str
#     contraseña: str
#     telefono: str

# @app.get("/user/info", tags=["Usuarios"])
# async def show_user_info():
#     list_users = []
    
#     db_connector.show_table_user(200)
#     for info_list in result:
#         user_info_instance = UserInfo(
#             id=info_list[0],
#             nombre=info_list[1],
#             apellido=info_list[2],
#             edad=info_list[7],
#             correo=info_list[3],
#             contraseña=info_list[4],
#             telefono=info_list[5]
#         )
#         list_users.append(user_info_instance)
#     return list_users

# @app.get("/user/info/{name}", tags=["Usuarios"])
# async def read_user_info_by_name(name: str):
    
#     result = db_connector.show_user_by_name(name)
#     return result

# @app.post("/user/create", tags=["Usuarios"])
# async def create_user_info(user: UserInfo):
    
#     user_create = db_connector.create_user(
#         name=user.nombre,
#         lastname=user.apellido,
#         age=user.edad,
#         email=user.correo,
#         password=user.contraseña,
#         phone=user.telefono
#     )
#     return user_create

# @app.put("/user/update", tags=["Usuarios"])
# async def update_user_info(user: UserInfo):
    
#     update_user= db_connector.update_user(
#         name=user.nombre,
#         lastname=user.apellido,
#         age=user.edad,
#         email=user.correo,
#         password=user.contraseña,
#         phone=user.telefono
#     )
#     return update_user

# @app.delete("/user/delete/{name}/{password}", tags=["Usuarios"])
# async def delete_user_info(name: str, password: str):
    
#     delete_user = db_connector.delete_user(name, password)
#     return delete_user

# # @app.post("/cookie-and-object/")
# # async def create_cookie(response: Response):
# #     response.set_cookie(key="fakesession", value="fake-cookie-session-value")
# #     return {"message": "Come to the dark side, we have cookies"}

# # @app.post("/cookie/")
# # async def create_cookie():
# #     content = {"message": "Come to the dark side, we have cookies"}
# #     response = JSONResponse(content=content)
# #     response.set_cookie(key="fakesession", value="fake-cookie-session-value")
# #     return response