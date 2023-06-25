from Usuario import *
from Persona import *
from Empresa import *
from Vacante import *
from Postulacion import *

'''usuario = Usuario ('Persona', 1234, '1234')
persona = Persona ('Persona', 1234, '4321', '6 meses', 'Valentina', 3123254685, 'avled@gmail', 'Calle47', 'Desempleado', 'Tecnologo', '10/10/2003')
empresa = Empresa ('001', 'Empresa@gmail', '142', 'Libre')
vacante = Vacante ('01', 'Analista y desarrollador de software', 5, 'Salario Minimo Legal Vigente', '10 Meses', 'Contrato Indefinido', 'Lunes a Viernes')
'''
postulacion = Postulacion ('Ecopetrol' , 'Vacantes = 5', 'postulaciones = 10', 'fecha de inicio = 10/05/2023', 'Fecha de cierre = 20/07/2023', 'Experiencia laboral de un año', 'situacion ocupacional: Desempleado', 'Tecnologo en Analisis y desarrollo de sofware' 'Salario minimo legal vigente', 'Conmtrato indefinido', 'Postulacion Abierta ' )

'''print(usuario.mostrar_usuario())
print(persona.mostrar_persona())
print(empresa.mostrar_empresa())
print(vacante.mostrar_vacante())'''
print(postulacion.mostar_postulacion())

postulacion.compara_cadidato_oferta()