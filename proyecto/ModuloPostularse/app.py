from Persona import *
from Empresa import *
from Vacante import *
from Postulacion import *

usuario = usuario('Persona', 1234, 'pass1')
persona = Persona('Persona', 1234, 'pass1', '1 año', 'valentin', 312, 'jskhs@gmail', 'Cra77', 'Desempleado', 'Tecnico', '17-08-2005')
empresa = Empresa ('002', 'empre@gmail.com', 12, 'privada')
vacante = Vacante('01', 'Desarrollador', 100, 'Salario Minimo','10 Meses', 'Contrato Fijo', 'Soacha', 'Lunes a Viernes')
postulacion = Postulacion ('12', 'ADSO', 100, '1500000', '6 meses', 'fijo', 'Soacha','lunes a viernes', 'abierta')
b1= True

while b1:
    opcion = int(input('Ingrese 1 si desea ver los usuarios o 2 si desea ver las vacantes:'))
    print()
    
    if opcion == 0:
        break
        
    elif opcion == 1:
        
        print ("usuario")
        
        print(usuario.mostrar_usuario())
        print(persona.mostrar_persona())
        print(empresa.mostrar_empresa())
        
    elif opcion == 2:
        print("Vacante") 
        print("Postulacion")
        print(vacante.mostrar_vacante())
        print(postulacion.mostrar_postulacion())