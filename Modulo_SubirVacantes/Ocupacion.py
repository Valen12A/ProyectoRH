from Vacante import Vacante

class Ocupacion(Vacante):
    def __init__(self, id, ocupacion, numVacante, salario, mesesExperiencia, tipoContrato, ubicacion, jornadaTrabajo, codigo, nombreCargo, funciones, descripcion, grupo_primario):
        super().__init__(id, ocupacion, numVacante, salario, mesesExperiencia, tipoContrato, ubicacion, jornadaTrabajo)
        self.__codigo = codigo
        self.__nombreCargo = nombreCargo
        self.__funciones = funciones
        self.__descripcion = descripcion
        self.__grupo_primario = grupo_primario
