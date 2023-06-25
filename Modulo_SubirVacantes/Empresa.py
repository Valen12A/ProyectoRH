from Usuario import *

class Empresa(Usuario):
    def __init__(self, tipoUsuario, numDocumento, contraseña, nit, email, numeroTrabajadores, tipoEmpresa):
        super().__init__(tipoUsuario, numDocumento, contraseña)
        self.__nit = nit
        self.__email = email
        self.__numeroTrabajadores = numeroTrabajadores
        self.__tipoEmpresa = tipoEmpresa
        self.__oferta = []
    
    def mostrar_empresa(self):
        return f'{self.__nit}, {self.__email}, {self.__numeroTrabajadores}, {self.__tipoEmpresa}'

    def SubirOferta():
        pass