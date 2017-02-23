from django.utils.translation import ugettext_lazy as _

dict_m2000 = {'Beginning':['Documentacion Inicial',
                                      'Inspeccion Visual',
                                      'Preparacion de Labview',
                                      'Chequeo preliminar de voltajes iniciales'],
                         'Program':['Programacion de Flasheo',
                                    'Conexion de arneces simulador del carro y arneces cartop',#if cartop
                                    'Programacion del Firmware',
                                    'Conexion de arneces del simulador',#if !cartop
                                    'Programacion del Solid State Starter',
                                    'Programacion de parametros F1',
                                    'Programacion tarjeta CE Electronics'],
                         'Logic':['Board power test SAFL & SAFS',
                                  'Motor Starter Test',
                                  'Valve control and limits',
                                  'Safety and inspection',
                                  'Door locks and hoistway access',
                                  'Landing system',
                                  'Door Interface (Pag CT1, CT2)',#if DCC
                                  'COP parte 1 (Pag CPI)',#if DCC
                                  'Door Interface (Pag 11, 11X)',#if !DCC
                                  'COP parte 1 (Pag 12)',#if !DCC
                                  'Fire Service Phase I (Pag 13)',
                                  'Fire Service Phase II (Pag 12)',#if !CPI
                                  'Movement Indication (Pag 14)',#if !CPI
                                  'Fire Service Phase II (Pag CPI)',#if CPI
                                  'Movement Indication (Pag CPI)',#if CPI
                                  'Car Calls (Pag CPI)',#if CPI
                                  'Calls (Pag 16)',
                                  'Serial Hall Calls (Pag SH)',#if serial hall calls
                                  'Programmable Input/Outputs'],
                         'Ending':['Inspeccion Final',
                                   'Passcode',
                                   'Papeleria Final',
                                   'Respaldo Electronico de la papeleria',
                                   'Desconnecion de Arneces',
                                   'Carro a estacion final'],
                         'Complete':['Fin de pruebas'],
                         'Stopped': ['Detenido']}
dict_m4000 = {'Beginning':['Documentacion Inicial',
                                      'Inspeccion Visual',
                                      'Preparacion de Labview',
                                      'Chequeo preliminar de voltajes iniciales'],
                         'Program':['Programacion de Flasheo',
                                    'Conexion de arneces simulador del carro y arneces cartop',#if cartop
                                    'Programacion del Firmware',
                                    'Conexion de arneces del simulador',#if !cartop
                                    'Programacion de parametros F1',
                                    'Programacion tarjeta CE Electronics',
                                    'Programacion de Parametros F7\n Version Test',
                                    'Programacion de Parametros F5\n Version Test',
                                    'MBRAKE Module\nCalibracion Inicial',
                                    'F5 Floor Learning',
                                    'F7 Terminal Limits'],
                         'Logic':['Board power test SAFL & SAFS',
                                  'Drive Interface',
                                  'Emergency Brake',
                                  'Safety and inspection',
                                  'Door locks and hoistway access',
                                  'Landing System',
                                  'Door Interface (Pag CT1, CT2)',#if DCC
                                  'COP parte 1 (Pag CPI)',#if DCC
                                  'Door Interface (Pag 11, 11X)',#if !DCC
                                  'COP parte 1 (Pag 12)',#if !DCC
                                  'Fire Service Phase I (Pag 13)',
                                  'Fire Service Phase II (Pag 12)',#if !CPI
                                  'Movement Indication (Pag 14)',#if !CPI
                                  'Fire Service Phase II (Pag CPI)',#if CPI
                                  'Movement Indication (Pag CPI)',#if CPI
                                  'Car Calls (Pag CPI)',#if CPI
                                  'Calls (Pag 16)',
                                  'Serial Hall Calls (Pag SH)',#if serial hall calls
                                  'Programmable Input/Outputs',
                                  'Additional Manual Test\n(Overspeeds and Limits)',
                                  'MBRAKE\nCalibracion Final',
                                  'Programacion de Parametros F7\n Version Cliente',
                                  'Programacion de Parametros F5\n Version Cliente',],
                         'Ending':['Inspeccion Final',
                                   'Passcode',
                                   'Papeleria Final',
                                   'Respaldo Electronico de la papeleria',
                                   'Desconnecion de Arneces',
                                   'Carro a estacion final'],
                         'Complete':['Fin de pruebas'],
                         'Stopped': ['Detenido']}
dict_elem = {'Beginning':['Configuracion Inicial de PC',
                          'Conseguir Software(Update) y Parametros(XML)',
                          'Crear Carpeta del Job y Crear Archivos de Documentacion:\nStarter REC, Board Information',
                          'Escanear Codigos de Barras de Tarjetas y Dispositivos',
                          'Crear Documentacion de Visual Inspection List, Tech Report y Passcode',
                          'Inspeccionar Jumpers y Switches',
                          'Checar Voltajes'],
                         'Program':['Flashear HAPS',#If HAPS
                                    'Cargar el Software(Update)',
                                    'Conectar Arneces',
                                    'Cargar Software en el LS-EDGE del Cliente',
                                    'Verificar Tolerancias de AC por Medio de LabView',
                                    'Cargar los Parametros(XML)',
                                    'Agregar y Modificar Datos de Test',
                                    'Prueba Automatizada de LabView'],
                         'Ending':['Respaldar Electronicamente el Reporte de Prueba Automatizada',
                                   'Devolver Parametros Originales de Cliente',
                                   'Extraer los Parametros(CCF)',
                                   'Introducir el Passcode',
                                   'Poner el Controlador en Construction Mode',
                                   'Imprimir Papeleria Final',
                                   'Hacer Respaldo Electronico de Documentos al Servidor',
                                   'Carro a Estacion Final'],
                         'Logic':[''],
                         'Complete':['Fin de pruebas'],
                         'Stopped': ['Detenido']}

times_m2000 = {'Beginning':60,
                         'Program':40,
                         'Logic':110,
                         'Ending':45}
times_m4000 = {'Beginning':240,
                         'Program':205,
                         'Logic':370,
                         'Ending':30}
times_elem = {'Beginning':40,
                         'Program':120,
                         'Ending':60}
stop_reasons = [('Job reassignment', 'Job reassignment'),
                ('Shift ended','Shift ended'),
                ('Error Funcional', 'Error Funcional'),
                ('Tarjetas T', 'Tarjetas T'),
                ('Material Faltante', 'Custom Software Faltante'),
                ('Junta de supervisor', 'Junta de supervisor'),
                ('Tecnico no asignado', 'Tecnico no asignado'),
                ('Personal', 'Personal'),
                ('Ingenieria', 'Ingenieria'),
                ('Falla en equipo de computo', 'Falla en equipo de computo'),
                ('Entrenamiento', 'Entrenamiento')]#TODO is this list still needed?
stations_dict = [('1', 'S1'),
                 ('2', 'S2'),
                 ('3', 'S3'),
                 ('4', 'S4'),
                 ('5', 'S5'),
                 ('6', 'S6'),
                 ('7', 'S7'),
                 ('8', 'S8'),
                 ('9', 'S9'),
                 ('10', 'S10'),
                 ('11', 'S11'),
                 ('12', 'S12'),
                 ('13', 'ELEM1'),
                 ('14', 'ELEM2')]
status_dict = [('Beginning', 'Beginning'),
               ('Program', 'Program'),
               ('Logic', 'Logic'),
               ('Ending', 'Ending'),
               ('Complete', 'Complete'),
               ('Stopped', 'Stopped')]
type_of_jobs = [('2000', 'M2000'),
                ('4000', 'M4000'),
                ('ELEM', 'Element')]
features_list = [('COP','Serial Car Operating Panel'),
                 ('SHC','Serial Hall Calls'),
                 ('HAPS','HAPS battery'),
                 ('OVL','Overlay'),
                 ('GROUP','Group'),
                 ('mView','mView'),
                 ('iMon','iMonitor'),
                 ('DCC',_('Door Control in Cartop')),
                 ('CPI',_('CPI Board Included'))]
features=(('COP','Serial Car Operating Panel'),
          ('SHC','Serial Hall Calls'),
          ('HAPS','HAPS Battery'),
          ('DCC',_('Door Control in Cartop')),
          ('CPI',_('CPI Board Included')),
          ('OVL','Overlay'),
          ('GROUP','Group'),
          ('mView','mView'),
          ('iMon','iMonitor'),
          ('None',_('None')))
stations = (('1', 'S1'),
            ('2', 'S2'),
            ('3', 'S3'),
            ('4', 'S4'),
            ('5', 'S5'),
            ('6', 'S6'),
            ('7', 'S7'),
            ('8', 'S8'),
            ('9', 'S9'),
            ('10', 'S10'),
            ('11', 'S11'),
            ('12', 'S12'),
            ('13', 'ELEM1'),
            ('14', 'ELEM2'))
label_admin = [('-', '-'),
               ('A', 'A'),
               ('B', 'B'),
               ('C', 'C'),
               ('D', 'D'),
               ('E', 'E'),
               ('F', 'F'),
               ('G', 'G'),
               ('H', 'H')]
label = (('-', '-'),
         ('A', 'A'),
         ('B', 'B'),
         ('C', 'C'),
         ('D', 'D'),
         ('E', 'E'),
         ('F', 'F'),
         ('G', 'G'),
         ('H', 'H'))
job_type = (('2000', 'M2000'),
            ('4000', 'M4000'),
            ('ELEM', 'Element'))