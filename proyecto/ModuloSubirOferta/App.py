from App import *
from Persona import *
from Empresa import *
from Vacante import *
from Ubicacion import *

usuario = Usuario('Persona', 1234, 'pass1')
persona = Persona('Persona', 1234, 'pass1', '1 año', 'Ronald', 312, 'ronald@gmail', 'Cra77', 'Desempleado', 'Tecnico', '17-08-2005')
empresa = Empresa('001', 'Empresa@gmail', '10', 'Libre')
ubicacion = Ubicacion('Cundinamarca', 'Soacha', '001', '0010')
vacante = Vacante('01', 'Desarrollador', 100, 'Salario Minimo', '10 Meses', 'Contrato Fijo', ubicacion, 'Lunes a Viernes')

print(usuario.mostrar_usuario())
print(persona.mostrar_persona())
print(empresa.mostrar_empresa())
print(vacante.mostrar_vacante())
persona.subirHojaVida()
empresa.SubirOferta()