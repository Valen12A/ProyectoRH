from vacante import *
from oferta import *
class Buscar(Vacante):
    def __init__( self,id,ocupacion,numVacante,salario,mesesExperiencia,tipoContrato,ubicacion,jornadaTrabajo,codigo,empresa,vacante,numPostulaciones,fechaInicio,fechaCierre,cargo,experiencia,rangoSalarial):
        Vacante().__init.__(id,ocupacion,numVacante,salario,mesesExperiencia,tipoContrato,ubicacion,jornadaTrabajo)
        Oferta().__init__(codigo,empresa,vacante,numPostulaciones,fechaInicio,fechaCierre)
        self.__cargo=cargo
        self.__ubicacion=ubicacion
        self.__experiencia=experiencia
        self.__rangoSalarial=rangoSalarial    
    
    # def buscarOfertas(Oferta):
    #     Buscar_codigo=int(input('Ingrese el codigo de la oferta a buscar: '))
    #     for Oferta.empleo in range:
    #         if self.__codigo == Buscar_codigo:
    #             print('El codigo ingresado concide con una vacante')
    #             print(f'la oferta con ese codigo  es: {Oferta.empleo}')
    #         else:
    #             print('El codigo no concide con la vacante')

    def buscarVacantes(Vacante):
        Buscar_id=int(input('Ingrese el id de la oferta a buscar: '))
        for Vacante  in range(len(Vacante.lista_cargos)):
            if Vacante.__id == Buscar_id:
                print('El id ingresado concide con una vacante')
                print(f'El cargo con ese id es: {Vacante.lista_cargos}')
            else:
                print('El id no concide con la vacante')


    def FiltrarOferta():
        pass