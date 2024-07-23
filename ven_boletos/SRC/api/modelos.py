from pydantic import BaseModel
from datetime import datetime


class model_asiento(BaseModel):
    sala: str
    numero_asiento: int
    seccion_asiento: str
    fecha_asiento: datetime


if __name__ == "__main__":
    pass