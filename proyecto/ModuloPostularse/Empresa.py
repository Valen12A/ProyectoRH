from Usuario import *

class Empresa(usuario):
    def __init__(self, nit,email,numTrabajadores,tipoEmpresa):
       # usuario().__init__(tipoUsuario, numDocumento,contraseña)
        self.__nit = nit
        self.__email = email
        self.__numTrabajadores = numTrabajadores
        self.__tipoEmpresa = tipoEmpresa
        self.__oferta = []

    def SubirOferta():
        pass

    def mostrar_empresa(self):
        return f'{self.__nit},{self.__email}, {self.__numTrabajadores}, {self.__tipoEmpresa}'