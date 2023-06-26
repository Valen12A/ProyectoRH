
from Vacante import *

class Postulacion (Vacante):
    def __init__(self, id, ocupacion, numVacante, salario, mesesExperiencia, tipoContrato, ubicacion,jornadaTrabajo, postulacionAbiertaCerrada):
        super().__init__(id,ocupacion,numVacante,salario,mesesExperiencia,tipoContrato,ubicacion,jornadaTrabajo)
        self.__postulacionAbiertaCerrada = postulacionAbiertaCerrada
    


    # def comparar_cadidato_oferta(self, persona):
    #     if isinstance (Postulacion, persona )
    #         return self.__Persona == Postulacion
    #     return False
    
    def mostrar_postulacion(self):
        return f'{self.__dict__}'
    

 
        
    
