class Vacante():
    lista_cargos=[]
    def __init__(self,id,ocupacion,numVacante,salario,mesesExperiencia,tipoContrato,ubicacion,jornadaTrabajo):
        self.__id=id 
        self.__ocupaciones = ocupaciones
        self.__numVacante = numVacante
        self.__salario = salario
        self.__mesesExperiencia = mesesExperiencia
        self.__tipoContrato = tipoContrato
        self.__ubicacion = ubicacion
        self.__jornadaTrabajo = jornadaTrabajo
        Vacante.lista_cargos=[]

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id
    
    def getOcupacion(self):
        return self.__ocupaciones
    def setOcupacion(self,ocupaciones):
        self.__ocupaciones=ocupaciones
    
    def getNumVacantes(self):
        return self.__numVacante
    def setNumVacantes(self,numVacante):
        self.__numVacante=numVacante
    
    def getSalario(self):
        return self.__salario
    def setSalario(self,salario):
        self.__salario=salario
    
    def getMesesExperiencia(self):
        return self.__mesesExperiencia
    def setMesesExperinecia(self,mesesExperiencia):
        self.__mesesExperiencia=mesesExperiencia
    
    def getTipoContrato(self):
        return self.__tipoContrato
    def setTipoContrato(self,tipoContrato):
        self.__tipoContrato=tipoContrato

    def agregar_una_vez(lista,lista_cargos):
        try:
            if id in Vacante.lista_cargos:
                raise ValueError('Ya hay una oferta con ese id')
            else:
                lista.append(Vacante.lista_cargos)
                return lista
        except ValueError as ve:
            print(f'Error: {ve}')
        
    def Vacante():
        while True:
            id=int(input('Ingrese un id: '))
            ocupaciones=input('ingrese una ocupacion: ')
            numVacante=int(input('Ingrese el numero de vacantes: '))
            salario=int(input('Ingrese el salario a pagar: '))
            mesesExperiencia=int(input('Ingrese los meses de experiencia necesarios: '))
            tipoContrato=input('Ingrese el tipo de contrato: ')
            ubicacion=input('Ingrese la ubicacion del trabajo: ')
            jornadaTrabajo=input('Ingrese la jornada de trabajo: ')
            fin=(input('\n(0 para finalizar):'))
            try:
                id = int(fin)
                if id == 0:
                    break
                else:
                    Vacante.agregar_una_vez(Vacante.lista_cargos,Vacante.lista_cargos)
            except ValueError:
                Vacante.agregar_una_vez(Vacante.lista_cargos, id)
        print(f'la vacante es:{Vacante.lista_cargos}')
        print()
