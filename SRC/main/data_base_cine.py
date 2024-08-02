import random
import datetime
import traceback
import threading
import mysql.connector
from faker import Faker

#Instancias necesarias
fake = Faker()
lock = threading.Lock()


class conexion_base_datos():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password="12345",
                database='cine'
            )
            if self.conexion.is_connected():
                print("Conexión exitosa. Datos de la conexión:\n"
                      f"host={self.conexion.server_host}\n"
                      f"port={self.conexion.server_port}\n"
                      f"user={self.conexion.user}\n"
                      f"database={self.conexion.database}\n"
                      )
            else:
                print("Conexión fallida.")
        except Exception as ex:
            print(f"Exception al conectar a la base de datos: {ex}")
            print(traceback.format_exc())
        finally:
            pass 

    def try_decorador(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as ex:
                print(f"Exception en la función {func.__name__}: {ex}")
                print(traceback.format_exc())
        return wrapper
    
    def verificar_conexion(self):
        try:
            if self.conexion.is_connected():
                print("Conexión exitosa. Datos de la conexión:\n"
                      f"host={self.conexion.server_host}\n"
                      f"port={self.conexion.server_port}\n"
                      f"user={self.conexion.user}\n"
                      f"database={self.conexion.database}\n"
                      )
                return self.conexion.is_connected()
            else:
                print("Conexión fallida.")
                return False
        except Exception as ex:
            print(f"Exception al verificar la conexión: {ex}")
            print(traceback.format_exc())
            return False

    def close_connection(self):
        try:
            if self.conexion.is_connected():
                self.conexion.close()
            return True
        except Exception as ex:
            print(f"Exception al cerrar la conexión: {ex}")
            print(traceback.format_exc())
            return False
    
    def anadir_sala(self, nombre_sala: str, capacidad_sala: int, estado_sala: int) -> bool:
        try:
            with self.conexion.cursor() as cursor:
                # Verificar si la sala ya existe
                verificar_sala = "SELECT * FROM salas WHERE nombre = %s AND capacidad = %s"
                valores_verificar_sala = (nombre_sala, capacidad_sala)
                cursor.execute(verificar_sala, valores_verificar_sala)
                
                if cursor.fetchone() is None:
                    # Si no existe, añadir la sala
                    anadir_sala = "INSERT INTO salas (nombre, capacidad, estado) VALUES (%s, %s, %s)"
                    cursor.execute(anadir_sala, (nombre_sala, capacidad_sala, estado_sala,))
                    self.conexion.commit()
                    return True
                else:
                    print("La sala ya existe")
                    return False
        except Exception as ex:
            print(f"Ha ocurrido un Exception:\n {ex}")
            print(traceback.format_exc())
            return False
        
    def anadir_asientos(self, nombre_sala: str, numero_asiento: int, seccion_asiento: str, fecha):
        try:
            with self.conexion.cursor() as cursor:
                # Verificar si la sala existe
                verificar_sala = "SELECT sala_id FROM salas WHERE nombre = %s"
                cursor.execute(verificar_sala, (nombre_sala,))
                resultado_sala = cursor.fetchone()

                if not resultado_sala:
                    print("No se ha encontrado la sala")
                    return False
                else:
                    id_sala_verificada = resultado_sala[0]  # Obtener el primer resultado y el primer campo (sala_id)

                # Verificar si hay un horario para la fecha dada
                verificar_horario_asiento = "SELECT horario_id FROM horarios WHERE fecha = %s AND sala_id = %s"
                cursor.execute(verificar_horario_asiento, (fecha, id_sala_verificada))
                resultado_busqueda_horario = cursor.fetchone()

                if not resultado_busqueda_horario:
                    print("No se ha encontrado el horario")
                    return False
                else:
                    id_horario = resultado_busqueda_horario[0]  # Obtener el primer resultado y el primer campo (horario_id)

                # Verificar si el asiento ya existe y está ocupado
                verificar_asientos = "SELECT estado FROM asientos WHERE numero_asiento = %s AND seccion = %s AND sala_id = %s"
                cursor.execute(verificar_asientos, (numero_asiento, seccion_asiento, id_sala_verificada))
                informacion_asientos = cursor.fetchone()

                if informacion_asientos and informacion_asientos[0] == 1:
                    print("El asiento ya está ocupado")
                    return False
                else:
                    # Insertar el nuevo asiento
                    agregar_asiento = """
                        INSERT INTO asientos (numero_asiento, seccion, sala_id, estado, horario_id) 
                        VALUES (%s, %s, %s, %s, %s)
                    """
                    valores_nuevo_asiento = (numero_asiento, seccion_asiento, id_sala_verificada, 1, id_horario)
                    cursor.execute(agregar_asiento, valores_nuevo_asiento)
                    self.conexion.commit()
                    print("Asiento añadido exitosamente")
                    return True
        except Exception as ex:
            print(f"Ha ocurrido un Exception:\n {ex}")
            print(traceback.format_exc())
            return False
        finally:
            pass

    def anadir_pelicula(self, titulo_pelicula: str, genero_pelicula: str, duracion_pelicula: int, rating_pelicula:int):
        try:
            with self.conexion.cursor() as cursor:
                verificar_pelicula = "SELECT * FROM peliculas WHERE titulo = %s"
                cursor.execute(verificar_pelicula, (titulo_pelicula,))
                if cursor.fetchone() is None:
                    anadir_pelicula = "INSERT INTO peliculas (titulo, genero, duracion, rating) VALUES (%s, %s, %s, %s)"
                    cursor.execute(anadir_pelicula, (titulo_pelicula, genero_pelicula, duracion_pelicula, rating_pelicula,))
                    self.conexion.commit()
                    print("Pelicula añadida")
                    return True
                else:
                    return False
        except Exception as ex:
                print(f"Ha ocurrido un Exception:\n {ex}")
                print(traceback.format_exc())
        finally:
            pass
        
    def anadir_cliente(self, nombre_cliente: str, apellido_cliente: str, correo_cliente: str, documento: str):
        try:
            with self.conexion.cursor() as cursor:
                
                verificar_cliente = "SELECT * FROM clientes WHERE documento = %s"
                cursor.execute(verificar_cliente, (documento,))
                resultado_verificacion_cliente = cursor.fetchall()
                
                if len(resultado_verificacion_cliente) == 0:
                    anadir_cliente = "INSERT INTO clientes (nombre, apellido, correo, documento) VALUES (%s, %s, %s, %s)"
                    valores_nuevo_cliente = (nombre_cliente, apellido_cliente, correo_cliente, documento)
                    cursor.execute(anadir_cliente, valores_nuevo_cliente)
                    self.conexion.commit()
                    print("Cliente añadido")
                    return True
                else:
                    print("El cliente ya existe")
                    return False
        except Exception as ex:
            print(f"Ha ocurrido un Exception:\n{ex}")
            print(traceback.format_exc())
            return False

    def anadir_horarios(self, nombre_pelicula: str, nombre_sala: str, fecha_date):
        try:
            with self.conexion.cursor() as cursor:
                # Verificar si la película existe
                busqueda_pelicula = "SELECT pelicula_id FROM peliculas WHERE titulo = %s"
                cursor.execute(busqueda_pelicula, (nombre_pelicula,))
                resultado_busqueda_pelicula = cursor.fetchall()

                if not resultado_busqueda_pelicula:
                    print("No se ha encontrado la película")
                    return False
                else:
                    pelicula_id = resultado_busqueda_pelicula[0][0]  # Obtener el primer resultado y el primer campo (pelicula_id)

                # Verificar si la sala existe y está disponible
                busqueda_sala = "SELECT sala_id FROM salas WHERE nombre = %s AND estado = %s"
                cursor.execute(busqueda_sala, (nombre_sala, 1,))
                resultado_busqueda_sala = cursor.fetchall()

                if not resultado_busqueda_sala:
                    print("No se ha encontrado la sala o no está disponible")
                    return False
                else:
                    sala_id = resultado_busqueda_sala[0][0]  # Obtener el primer resultado y el primer campo (sala_id)

                
                # Verificar si el horario ya está registrado
                busqueda_horario = """
                    SELECT * FROM horarios 
                    WHERE pelicula_id = %s AND sala_id = %s AND fecha = %s 
                """
                cursor.execute(busqueda_horario, (pelicula_id, sala_id, fecha_date,))
                resultado_busqueda_horario = cursor.fetchall()
                
                if resultado_busqueda_horario is None:
                    print("El horario ya está registrado para esta película y sala")
                    return False
                else:
                    # Insertar el horario si no está duplicado
                    insertar_horario = "INSERT INTO horarios (pelicula_id, sala_id, fecha) VALUES ( %s, %s, %s)"
                    cursor.execute(insertar_horario, (pelicula_id, sala_id, fecha_date, ))
                    self.conexion.commit()
                    print("Horario añadido exitosamente")
                    return True
        except Exception as e:
            print(f"Exception al añadir el horario: {e}")
            return False
        finally:
            pass
  
    def agregar_venta(self, documento_cliente: int, nombre_pelicula: int, horario_pelicula: int, numero_asiento: int, seccion_asiento:str):
        try:
            with self.conexion.cursor() as cursor:
                # Verificar si el cliente existe
                busqueda_cliente = "SELECT cliente_id FROM clientes WHERE documento = %s"
                cursor.execute(busqueda_cliente, documento_cliente)
                resultado_busqueda_cliente = cursor.fetchone()
                
                
                if resultado_busqueda_cliente is None:
                    print("No se ha encontrado el cliente")
                    return False
                else:
                    id_cliente = resultado_busqueda_cliente['cliente_id']
                
                # Verificar si la película existe
                busqueda_pelicula = "SELECT pelicula_id FROM peliculas WHERE titulo = %s"
                cursor.execute(busqueda_pelicula, nombre_pelicula)
                resultado_busqueda_pelicula = cursor.fetchone()
                
                if resultado_busqueda_pelicula is None:
                    print("No se ha encontrado la película")
                    return False
                else:
                    id_pelicula = resultado_busqueda_pelicula['pelicula_id']
                
                # Verificar si el horario existe
                busqueda_horario = "SELECT horario_id FROM horarios WHERE fecha= %s"
                cursor.execute(busqueda_horario, horario_pelicula)
                resultado_busqueda_horario = cursor.fetchone()
                
                if resultado_busqueda_horario is None:
                    print("No se ha encontrado el horario")
                    return False
                else:
                    id_horario = resultado_busqueda_horario['horario_id']
                
                # Verificar si el asiento existe
                busqueda_asiento = "SELECT * FROM asientos WHERE numero_asiento = %s AND seccion = %s"
                cursor.execute(busqueda_asiento, numero_asiento, seccion_asiento)
                resultado_busqueda_asiento = cursor.fetchone()
                
                if resultado_busqueda_asiento is None:
                    print("No se ha encontrado el asiento")
                    return False
                else:
                    id_asiento = resultado_busqueda_asiento['asiento_id']

                # # Verificar si el asiento ya está reservado para ese horario
                # busqueda_asiento_reservado = """
                #     SELECT * FROM ventas 
                #     WHERE horario_id = %s AND asiento_id = %s
                # """
                # cursor.execute(busqueda_asiento_reservado, (horario_id, asiento_id))
                # resultado_asiento_reservado = cursor.fetchone()
                
                # if resultado_asiento_reservado is not None:
                #     print("El asiento ya está reservado para este horario")
                #     return False
                
                # # Insertar la venta si todas las verificaciones son exitosas
                # fecha_venta = datetime.date.today()
                # insertar_venta = """
                #     INSERT INTO ventas (cliente_id, pelicula_id, horario_id, fecha_venta, asiento_id) 
                #     VALUES (%s, %s, %s, %s, %s)
                # """
                # valores_insertar_venta = (cliente_id, pelicula_id, horario_id, fecha_venta, asiento_id)
                # cursor.execute(insertar_venta, valores_insertar_venta)
                # self.conexion.commit()
                
                # print("Venta agregada exitosamente")
                return True
                
        except Exception as e:
            print(f"Exception al agregar la venta: {e}")
            return False
        
    def llenar_datos_falsos_salas(self, num_salas: int):
        for _ in range(num_salas):
            nombre_sala = fake.company()  # Nombre ficticio de la sala
            capacidad_sala = random.randint(50, 200)  # Capacidad aleatoria entre 50 y 200
            estado_sala = random.choice([1, 1])  # Estado aleatorio

            # Llamar a la función anadir_sala con los datos falsos generados
            resultado = self.anadir_sala(nombre_sala, capacidad_sala, estado_sala)
            if resultado:
                print(f"Sala añadida: {nombre_sala}, Capacidad: {capacidad_sala}, Estado: {estado_sala}")

    def llenar_datos_falsos_clientes(self, numero_clientes_falsos: int):
        try:
            for _ in range(numero_clientes_falsos):
                nombre = fake.name()
                apellido = fake.last_name()
                correo = fake.email()
                documento = fake.ssn()

                resultado = self.anadir_cliente(nombre, apellido, correo, documento)
                if resultado:
                    print(f"Cliente añadido: {nombre} {apellido}, Correo: {correo}, Documento: {documento}")
                else:
                    print(f"Exception al añadir cliente ficticio")
        except Exception as ex:
            print(f"Ha ocurrido un Exception:\n{ex}")
            print(traceback.format_exc())

    def llenar_datos_falsos_peliculas(self, numero_peliculas_falsas: int):
        try:
            for _ in range(numero_peliculas_falsas):
                titulo = fake.catch_phrase()
                genero = fake.word()
                duracion = fake.random_int(min=60, max=180)
                rating = fake.random_int(min=1, max=10)

                resultado = self.anadir_pelicula(titulo, genero, duracion, rating)
                if resultado:
                    print(f"Película añadida: {titulo}, Género: {genero}, Duración: {duracion}, Rating: {rating}")
                else:
                    print(f"Exception al añadir película ficticia")
        except Exception as ex:
            print(f"Ha ocurrido un Exception:\n{ex}")
            print(traceback.format_exc())

    def buscar_peliculas(self):
        try:
            with self.conexion.cursor() as cursor:
                busqueda_titulos = "SELECT titulo FROM cine.peliculas"
                cursor.execute(busqueda_titulos)
                resultado_busqueda_titulos = cursor.fetchall()
                Lista_titulos = []                
                if not resultado_busqueda_titulos:
                    print("No se ha encontrado ningún título")
                    return Lista_titulos
                else:
                    for titulo in resultado_busqueda_titulos:
                        titulo_pelicula = titulo[0]
                        Lista_titulos.append(titulo_pelicula)
                    return Lista_titulos 
        except Exception as ex:
            print(f"Ha ocurrido un Exception:\n{ex}")
            import traceback
            print(traceback.format_exc())
    
    def buscar_salas(self):
        try:
            with self.conexion.cursor() as cursor:
                busqueda_sala = "SELECT nombre FROM cine.salas"
                cursor.execute(busqueda_sala)
                
                resultado_busqueda_salas = cursor.fetchall()
                lista_salas = []
                if not resultado_busqueda_salas:
                    print("No se ha encontrado ningún título")
                    return lista_salas
                else:
                    for nombre in resultado_busqueda_salas:
                        lista_salas.append([nombre][0][0])
                    return lista_salas 
        except Exception as ex:
            print(f"Ha ocurrido un Exception:\n{ex}")
            print(traceback.format_exc())
    
    def buscar_fechas(self):
        try:
            with self.conexion.cursor() as cursor:
                busqueda_fecha = "SELECT fecha FROM cine.horarios"
                cursor.execute(busqueda_fecha)
                
                resultado_busqueda_fechas = cursor.fetchall()
                lista_fechas = []
                if not resultado_busqueda_fechas:
                    print("No se ha encontrado ningún título")
                    return lista_fechas
                else:
                    for fecha in resultado_busqueda_fechas:
                        fecha_sin_parsear= [fecha][0][0]
                        fecha_parseada = fecha_sin_parsear.strftime('%Y-%m-%d %H:%M:%S')
                        lista_fechas.append(fecha_parseada)
                    return lista_fechas            
        except Exception as ex:
            print(f"Ha ocurrido un Exception:\n{ex}")
            print(traceback.format_exc())    

    def llenar_datos_falsos_horarios(self, cantidad_horarios_falsos: int):
        try:
            fake = Faker()
            lista_peliculas = self.buscar_peliculas()
            lista_salas = self.buscar_salas()
            
            for _ in range(cantidad_horarios_falsos):
                # Genera una fecha aleatoria para abril de 2024
                fecha_falsa = fake.date_time_between_dates(datetime_start=datetime.datetime(2024, 4, 1),
                                                        datetime_end=datetime.datetime(2024, 4, 30))
                
                nombre_pelicula = random.choice(lista_peliculas)
                nombre_sala = random.choice(lista_salas)
                
                resultado = self.anadir_horarios(nombre_pelicula, nombre_sala, fecha_falsa.strftime('%Y-%m-%d %H:%M'))
                
                if resultado:
                    print(f"Horario creado: título: {nombre_pelicula}; sala: {nombre_sala}; fecha: {fecha_falsa}")
                else:
                    print(f"No se ha podido crear el horario datos\n pelicula: {nombre_pelicula}; sala: {nombre_sala}; fecha: {fecha_falsa}")
        
        except Exception as ex:
            print(f"Ha ocurrido una excepción:\n{ex}")
            print(traceback.format_exc())

    def llenar_datos_falsos_asientos(self, numero_asientos_falsos: int):
        try:
            lista_nombre_peliculas = self.buscar_peliculas()
            lista_fechas_peliculas = self.buscar_fechas()
            for _ in range(numero_asientos_falsos):
                numero_asiento_falso = random.randint(1, 50)
                seccion_asiento_falso = fake.random_letter()
                numero_random = random.randint(1, 2)
                nombre_sala = lista_nombre_peliculas[numero_random]
                fecha_random = lista_fechas_peliculas[numero_random]
                resultado = self.anadir_asientos(nombre_sala, numero_asiento_falso, seccion_asiento_falso, fecha_random)
                if resultado:
                    print(f"Asiento añadido: sala: {nombre_sala}; número: {numero_asiento_falso}; sección: {seccion_asiento_falso}; fecha: {fecha_random}")
                else:
                    print(f"No se ha podido añadir el asiento: sala: {nombre_sala}; número: {numero_asiento_falso}; sección: {seccion_asiento_falso}; fecha: {fecha_random}")
        except Exception as ex:
            print(f"Ha ocurrido una excepción:\n{ex}")
            print(traceback.format_exc())
        finally:
            pass
        
    def eliminar_horarios(self, numero_registros:int ):
        try:
            for i in range (numero_registros): 
                with self.conexion.cursor() as cursor:
                    query ="delete from cine.horarios WHERE horario_id = %s"
                    cursor.execute(query, (i,))
                    self.conexion.commit()
                    print(f"Eliminado{i}")
        except Exception as ex:
            print(f"Ha ocurrido una excepción:\n{ex}")
            print(traceback.format_exc())
        finally:
            pass
    
        
if __name__ == '__main__':
    #INSTACIA DE LA CLASE:
    base_datos = conexion_base_datos()
    #pruebas de cine y de github
    #Funciones de relleno:
    # Llenar la base de datos con 10 salas ficticias
    # base_datos.llenar_datos_falsos_salas(3000)
    # base_datos.llenar_datos_falsos_clientes(1000)
    # base_datos. llenar_datos_falsos_peliculas(1000)
    # base_datos.llenar_datos_falsos_horarios(1000)
    base_datos.llenar_datos_falsos_asientos(50)
    
    #Cerrar la conexion
    base_datos.close_connection()