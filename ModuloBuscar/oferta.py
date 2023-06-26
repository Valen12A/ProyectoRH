class Oferta:
    empleo=[]
    def __init__(self,codigo,empresa,vacantes,numPostulaciones,fechaInicio,fechaCierre):
        self.__codigo=codigo
        self.__empresa = empresa
        self.__vacantes = vacantes
        self.__numPostulaciones = numPostulaciones
        self.__fechaInicio = fechaInicio
        self.__fechaCierre = fechaCierre
        Oferta.empleo=[]
    
    def getCodigo(self):
        return self.__codigo
        def setCodigo(self,codigo):
            self.__codigo=id

    def getEmpresa(self):
        return self.__empresa
    def setEmpresa(self,empresa):
        self.__empresa=empresa
    
    def getVacantes(self):
        return self.__vacante
    def setVacantes(self,vacante):
        self.__vacante=vacante
    
    def getNumPostulados(self):
        return self.__numPostulaciones
    def setNumPostulados(self,numPostulaciones):
        self.__numPostulaciones=numPostulaciones
    
    def getFchaInicio(self):
        return self.__fechaInicio
    def setFechaInicio(self,fechaInicio):
        self.__fechaInicio=fechaInicio
    
    def getFechaCierre(self):
        return self.__fechaCierre
    def setFechaCierre(self,fechaCierre):
        self.__fechaCierre=fechaCierre
    
    # def agregar_una_vez(lista,empleo):
    #     try:
    #         if id in Oferta.empleo:
    #             raise ValueError('Ya hay una oferta con ese id')
    #         else:
    #             lista.append(Oferta.empleo)
    #             return lista
    #     except ValueError as ve:
    #         print(f'Error: {ve}')

    # def Ofertas():
    #     while True:
    #         id=int(input('Ingrese el id de la oferta:'))
    #         empresa=input('Ingrese el nombre de la empresa: ')
    #         vacantes=int(input('Ingrese el numero de vacantes:'))
    #         numPostulaciones=12
    #         fechaInicio=(input('Ingrese la fecha de inicio de la vacante: '))
    #         fechaCierre=(input('Ingrese la fecha de cierre de la vacante: '))
    #         fin=(input('\n(0 para finalizar):'))
    #         try:
    #             id == int(fin)
    #             if id == 0:
    #                 break
    #             else:
    #                 Oferta.agregar_una_vez(Oferta.empleo,Oferta.empleo)
    #         except ValueError:
    #             Ofertas.agregar_una_vez(Oferta.empleo, id)
    #     print(f'La oferta es {Ofertas.empleo}')
    #     print()
    def getDatos6(self):
        return f'{self.__codigo},{self.__empresa},{self.__vacantes},{self.__numPostulaciones},{self.__fechaInicio},{self.__fechaCierre}'
    
    def filtrarOferta():
        pass