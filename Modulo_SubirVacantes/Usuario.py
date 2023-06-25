class Usuario:
    def __init__(self, tipoUsuario, numDocumento, contraseña):
        self.__tipoUsuario = tipoUsuario
        self.__numDocumento = numDocumento
        self.__contraseña = contraseña

    def mostrar_usuario(self):
        return f'{self.__tipoUsuario}, {self.__numDocumento}, {self.__contraseña}'

    def iniciarSesion():
        pass

    def accederModulos():
        pass