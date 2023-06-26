class Ubicacion:
    def __init__(self, nombreDepartamento, nombreMunicipio, codigoDepartamento, codigoMunicipio):
        self.__nombreDepartamento = nombreDepartamento
        self.__nombreMunicipio = nombreMunicipio
        self.__codigoDepartamento = codigoDepartamento
        self.__codigoMunicipio = codigoMunicipio
    
    def mostrar_ubicacion(self):
        return f'{self.__nombreDepartamento}, {self.__nombreMunicipio}, {self.__codigoDepartamento}, {self.__codigoMunicipio}'