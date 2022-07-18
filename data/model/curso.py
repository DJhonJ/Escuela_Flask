class Curso:
    def __init__(self, id, nombre, estado, fecha_creacion, fecha_modificacion):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_estado(self):
        return self.estado

    def get_fecha_creacion(self):
        return self.fecha_creacion

    def get_fecha_modificacion(self):
        return self.fecha_modificacion

    def __str__(self) -> str:
        return f'{self.nombre}, {self.id}'