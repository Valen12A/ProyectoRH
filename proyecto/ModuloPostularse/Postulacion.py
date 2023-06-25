from Oferta import *
from Persona import *
from Vacante import *
class Postulacion (Oferta, Persona, Vacante):
    def __init__(self, empresa, numPostulaciones, fechaInicio, fechaCierre, experienciaLaboral, situacionOcupacional, estudios, ocupacion, numVacante, salario, tipoContrato, postulacionAbiertaCerrada,):
        Oferta().__init__(empresa, numPostulaciones, fechaInicio, fechaCierre)
        Persona().__init__( experienciaLaboral, situacionOcupacional, estudios)
        Vacante().__init__(ocupacion,numVacante,salario,tipoContrato)
        self.__postulacionAbiertaCerrada = postulacionAbiertaCerrada
    
    persona = Persona 

    def compara_cadidato_oferta(self, persona):
        if isinstance (Postulacion, persona ):
            return self.__Persona == Postulacion
        return False

 
        
    
