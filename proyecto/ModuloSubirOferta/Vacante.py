class Vacante():
    def __init__(self,id,ocupacion,numVacante,salario,mesesExperiencia,tipoContrato,ubicacion,jornadaTrabajo):
        self.__id = id
        self.__ocupacion = ocupacion
        self.__numVacante = numVacante
        self.__salario = salario
        self.__mesesExperiencia = mesesExperiencia
        self.__tipoContrato = tipoContrato
        self.__ubicacion = ubicacion
        self.__jornadaTrabajo = jornadaTrabajo

    def mostrar_vacante(self):
        return f'{self.__id}, {self.__ocupacion}, {self.__numVacante}, {self.__salario}, {self.__mesesExperiencia}, {self.__tipoContrato}, {self.__ubicacion}, {self.__jornadaTrabajo}'