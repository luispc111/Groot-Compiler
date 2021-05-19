
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARCO CARACTER CARACTERVAL CIRCULO COLOR COMA DESDE DIFQUE DIV DOSPUNTOS ENTERO ENTEROVAL ENTONCES ESCRIBIR FLOTANTE FLOTANTEVAL FUNCION GROSOR HACER HASTA ID IGUAL IGUALQUE LEER LETRERO LINEA L_CORCHETE L_LLAVE L_PAR MAS MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MENOS MIENTRAS MULT OR PENDOWN PENUP PRINCIPAL PROGRAMA PUNTO PUNTOXY PUNTOYCOMA REGRESA R_CORCHETE R_LLAVE R_PAR SI SINO VARIABLES VOID\n    program : PROGRAMA ID PUNTOYCOMA variables funciones PRINCIPAL L_PAR R_PAR bloque empty\n    \n    variables : VARIABLES variablesU\n              | empty\n\n    variablesU : variablesD\n               | empty\n    \n    variablesD : ID COMA variablesD\n               | ID DOSPUNTOS tipo_var PUNTOYCOMA variablesU\n    \n    funciones : funcionesU\n              | empty\n    \n    funcionesU : tipo_funcion FUNCION ID L_PAR recibir_parametros R_PAR variables bloque funcionesD\n    \n    funcionesD : funciones\n               | empty\n    \n    tipo_funcion : ENTERO empty\n                 | FLOTANTE empty\n                 | CARACTER empty\n                 | VOID empty\n    \n    tipo_var : ENTERO empty\n             | FLOTANTE empty\n             | CARACTER empty\n    \n    recibir_parametros : ID DOSPUNTOS tipo_var recibir_parametrosD empty\n                       | empty\n\n    recibir_parametrosD : COMA recibir_parametros empty\n                       | empty\n    \n    mandar_parametros : ID mandar_parametrosD empty\n                      | empty\n\n    mandar_parametrosD : COMA mandar_parametros empty\n                       | empty\n    \n    bloque : L_LLAVE bloqueU R_LLAVE empty\n\n    bloqueU : estatuto bloqueD empty\n            | empty\n\n    bloqueD : bloqueU empty\n            | empty\n    \n    estatuto : asignacion PUNTOYCOMA empty\n             | llamada PUNTOYCOMA empty\n             | retorno PUNTOYCOMA empty\n             | lectura PUNTOYCOMA empty\n             | escritura PUNTOYCOMA empty\n             | decision empty\n             | condicional empty\n             | no_condicional empty\n             | funciones_especiales PUNTOYCOMA empty\n             | empty\n    \n    asignacion : ID IGUAL exp empty\n    \n    llamada : ID L_PAR mandar_parametros R_PAR empty\n    \n    retorno : REGRESA L_PAR ID R_PAR empty\n    \n    lectura : LEER L_PAR exp R_PAR empty\n    \n    escritura : ESCRIBIR L_PAR escrituraD R_PAR empty\n\n    escrituraD : exp empty\n               | LETRERO empty\n    \n    decision : SI L_PAR R_PAR ENTONCES bloque SINO bloque empty\n    \n    condicional : MIENTRAS L_PAR exp R_PAR HACER bloque empty\n    \n    no_condicional : DESDE L_PAR asignacion R_PAR HASTA exp HACER bloque empty\n    \n    funciones_especiales : circulo empty\n                         | color empty\n                         | grosor empty\n                         | linea empty\n                         | puntoxy empty\n                         | arco empty\n                         | penup empty\n                         | pendown empty\n                         | empty\n    \n    circulo : CIRCULO L_PAR exp R_PAR empty\n    \n    color : COLOR L_PAR exp R_PAR empty\n    \n    grosor : GROSOR L_PAR exp R_PAR empty\n    \n    linea : LINEA L_PAR exp COMA exp COMA exp COMA exp R_PAR empty\n    \n    puntoxy : PUNTOXY L_PAR exp COMA exp R_PAR empty\n    \n    arco : ARCO L_PAR exp R_PAR empty\n    \n    penup : PENUP L_PAR exp R_PAR empty\n    \n    pendown : PENDOWN L_PAR exp R_PAR empty\n    \n    operadorA : MAS empty\n              | MENOS empty\n    \n    operadorT : MULT empty\n              | DIV empty\n    \n    operadorL : OR empty\n              | AND empty\n    \n    operadorR : MENORQUE empty\n              | MAYORQUE empty\n              | MENORIGUALQUE empty\n              | MAYORIGUALQUE empty\n              | IGUALQUE empty\n              | DIFQUE empty\n    \n    exp : termino expU empty\n    \n    expU : operadorA exp empty\n         | empty\n    \n    termino : factor terminoU empty\n\n    terminoU : operadorT termino empty\n             | empty\n    \n    factor : L_PAR expresion R_PAR empty\n            | factorU\n\n    factorU : operadorA factorD\n            | factorD\n\n    factorD : varcte empty\n    \n    varcte  : ID empty\n            | ENTEROVAL empty\n            | FLOTANTEVAL empty\n            | CARACTERVAL empty\n    \n    expresion  : exp expresionU\n\n    expresionU : operadorR expresion_dos empty\n               | empty\n    \n    expresion_dos  : exp expresion_dosU\n\n    expresion_dosU : operadorL exp empty\n                   | empty\n    \n    empty : \n    '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,41,47,85,124,],[0,-103,-1,-103,-28,]),'ID':([2,7,21,26,36,37,42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,114,115,116,117,118,119,120,121,124,127,128,129,130,131,132,137,139,141,142,169,175,178,179,180,184,185,192,205,206,219,220,223,225,226,227,228,229,230,239,254,255,256,257,258,259,262,264,268,270,271,272,273,278,279,280,281,282,284,],[3,19,29,19,43,19,60,-42,60,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,133,147,150,133,133,133,158,133,133,133,133,133,133,133,133,-28,-33,-34,-35,-36,-37,-41,133,133,-103,-103,43,133,133,-103,-103,-70,-71,147,133,133,-72,-73,133,-103,-103,-103,-103,-103,-103,133,-76,-77,-78,-79,-80,-81,-103,133,133,-103,-103,-103,-51,-74,-75,-50,-103,133,-52,]),'PUNTOYCOMA':([3,31,32,33,34,38,39,40,42,49,50,51,52,53,54,55,56,57,58,59,67,68,69,70,71,72,73,74,85,87,89,90,91,92,93,94,95,96,97,106,107,108,109,110,111,112,113,124,127,128,129,130,131,132,133,134,135,136,138,140,143,144,145,146,171,172,173,174,176,177,183,186,187,188,189,193,194,195,196,202,203,204,207,208,209,215,216,217,218,221,233,234,235,236,240,241,242,245,246,247,249,250,251,262,265,272,273,276,280,281,284,286,287,],[4,37,-103,-103,-103,-17,-18,-19,-103,-42,-103,89,90,91,92,93,-103,-103,-103,97,-103,-103,-103,-103,-103,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-53,-54,-55,-56,-57,-58,-59,-60,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-103,-89,-91,-103,-103,-103,-103,-93,-43,-103,-84,-103,-87,-90,-92,-94,-95,-96,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-82,-103,-85,-103,-103,-44,-45,-46,-47,-62,-63,-64,-67,-68,-69,-83,-86,-88,-103,-103,-103,-51,-66,-50,-103,-52,-103,-65,]),'VARIABLES':([4,84,],[7,7,]),'ENTERO':([4,5,6,7,16,17,18,27,30,37,46,83,85,124,170,],[-103,12,-3,-103,-2,-4,-5,32,-6,-103,-7,32,-103,-28,12,]),'FLOTANTE':([4,5,6,7,16,17,18,27,30,37,46,83,85,124,170,],[-103,13,-3,-103,-2,-4,-5,33,-6,-103,-7,33,-103,-28,13,]),'CARACTER':([4,5,6,7,16,17,18,27,30,37,46,83,85,124,170,],[-103,14,-3,-103,-2,-4,-5,34,-6,-103,-7,34,-103,-28,14,]),'VOID':([4,5,6,7,16,17,18,30,37,46,85,124,170,],[-103,15,-3,-103,-2,-4,-5,-6,-103,-7,-103,-28,15,]),'PRINCIPAL':([4,5,6,7,8,9,10,16,17,18,30,37,46,85,124,170,212,213,214,],[-103,-103,-3,-103,20,-9,-8,-2,-4,-5,-6,-103,-7,-103,-28,-103,-10,-11,-9,]),'L_LLAVE':([6,7,16,17,18,30,35,37,46,84,123,199,238,261,274,],[-3,-103,-2,-4,-5,-6,42,-103,-7,-103,42,42,42,42,42,]),'FUNCION':([11,12,13,14,15,22,23,24,25,],[21,-103,-103,-103,-103,-13,-14,-15,-16,]),'COMA':([19,32,33,34,38,39,40,122,133,135,136,138,140,143,144,145,146,147,162,163,171,173,174,176,177,183,186,187,188,189,215,216,217,218,221,243,249,250,251,275,],[26,-103,-103,-103,-17,-18,-19,169,-103,-103,-103,-89,-91,-103,-103,-103,-103,192,205,206,-93,-103,-84,-103,-87,-90,-92,-94,-95,-96,-82,-103,-85,-103,-103,264,-83,-86,-88,282,]),'DOSPUNTOS':([19,43,],[27,83,]),'L_PAR':([20,29,60,61,62,63,64,65,66,75,76,77,78,79,80,81,82,98,101,102,104,114,115,116,117,118,119,120,121,137,141,142,175,178,179,180,184,185,205,206,219,220,223,225,226,227,228,229,230,239,254,255,256,257,258,259,264,268,270,271,278,279,282,],[28,36,99,100,101,102,103,104,105,114,115,116,117,118,119,120,121,137,137,137,137,137,137,137,137,137,137,137,137,137,-103,-103,137,137,-103,-103,-70,-71,137,137,-72,-73,137,-103,-103,-103,-103,-103,-103,137,-76,-77,-78,-79,-80,-81,137,137,-103,-103,-74,-75,137,]),'R_PAR':([28,32,33,34,36,38,39,40,44,45,99,103,122,133,134,135,136,138,140,143,144,145,146,147,148,149,150,151,152,153,154,156,157,159,160,161,164,165,166,167,168,169,171,172,173,174,176,177,181,182,183,186,187,188,189,190,191,192,197,198,210,211,215,216,217,218,221,222,224,231,232,244,248,249,250,251,252,253,260,266,267,269,277,283,285,],[35,-103,-103,-103,-103,-17,-18,-19,84,-21,-103,155,-103,-103,-103,-103,-103,-89,-91,-103,-103,-103,-103,-103,193,-25,194,195,196,-103,-103,200,201,202,203,204,207,208,209,-103,-23,-103,-93,-43,-103,-84,-103,-87,221,-103,-90,-92,-94,-95,-96,-103,-27,-103,-48,-49,-20,-103,-82,-103,-85,-103,-103,-97,-99,-24,-103,265,-22,-83,-86,-88,-103,-103,-26,-98,-100,-102,-103,-101,286,]),'R_LLAVE':([42,48,49,50,56,57,58,85,86,87,88,89,90,91,92,93,94,95,96,97,124,125,126,127,128,129,130,131,132,262,272,273,280,281,284,],[-103,85,-30,-103,-103,-103,-103,-103,-103,-30,-103,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-29,-31,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'REGRESA':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[61,-42,61,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'LEER':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[62,-42,62,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'ESCRIBIR':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[63,-42,63,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'SI':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[64,-42,64,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'MIENTRAS':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[65,-42,65,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'DESDE':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[66,-42,66,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'CIRCULO':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[75,-42,75,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'COLOR':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[76,-42,76,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'GROSOR':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[77,-42,77,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'LINEA':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[78,-42,78,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'PUNTOXY':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[79,-42,79,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'ARCO':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[80,-42,80,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'PENUP':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[81,-42,81,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'PENDOWN':([42,49,50,56,57,58,85,87,89,90,91,92,93,94,95,96,97,124,127,128,129,130,131,132,262,272,273,280,281,284,],[82,-42,82,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-51,-50,-103,-52,]),'IGUAL':([60,158,],[98,98,]),'SINO':([85,124,237,],[-103,-28,261,]),'MAS':([98,101,102,104,114,115,116,117,118,119,120,121,133,135,136,137,138,140,141,142,143,144,145,146,171,175,176,177,178,179,180,183,184,185,186,187,188,189,205,206,217,218,219,220,221,223,225,226,227,228,229,230,239,250,251,254,255,256,257,258,259,264,268,270,271,278,279,282,],[141,141,141,141,141,141,141,141,141,141,141,141,-103,141,-103,141,-89,-91,-103,-103,-103,-103,-103,-103,-93,141,-103,-87,141,-103,-103,-90,-70,-71,-92,-94,-95,-96,141,141,-85,-103,-72,-73,-103,141,-103,-103,-103,-103,-103,-103,141,-86,-88,-76,-77,-78,-79,-80,-81,141,141,-103,-103,-74,-75,141,]),'MENOS':([98,101,102,104,114,115,116,117,118,119,120,121,133,135,136,137,138,140,141,142,143,144,145,146,171,175,176,177,178,179,180,183,184,185,186,187,188,189,205,206,217,218,219,220,221,223,225,226,227,228,229,230,239,250,251,254,255,256,257,258,259,264,268,270,271,278,279,282,],[142,142,142,142,142,142,142,142,142,142,142,142,-103,142,-103,142,-89,-91,-103,-103,-103,-103,-103,-103,-93,142,-103,-87,142,-103,-103,-90,-70,-71,-92,-94,-95,-96,142,142,-85,-103,-72,-73,-103,142,-103,-103,-103,-103,-103,-103,142,-86,-88,-76,-77,-78,-79,-80,-81,142,142,-103,-103,-74,-75,142,]),'ENTEROVAL':([98,101,102,104,114,115,116,117,118,119,120,121,137,139,141,142,175,178,179,180,184,185,205,206,219,220,223,225,226,227,228,229,230,239,254,255,256,257,258,259,264,268,270,271,278,279,282,],[144,144,144,144,144,144,144,144,144,144,144,144,144,144,-103,-103,144,144,-103,-103,-70,-71,144,144,-72,-73,144,-103,-103,-103,-103,-103,-103,144,-76,-77,-78,-79,-80,-81,144,144,-103,-103,-74,-75,144,]),'FLOTANTEVAL':([98,101,102,104,114,115,116,117,118,119,120,121,137,139,141,142,175,178,179,180,184,185,205,206,219,220,223,225,226,227,228,229,230,239,254,255,256,257,258,259,264,268,270,271,278,279,282,],[145,145,145,145,145,145,145,145,145,145,145,145,145,145,-103,-103,145,145,-103,-103,-70,-71,145,145,-72,-73,145,-103,-103,-103,-103,-103,-103,145,-76,-77,-78,-79,-80,-81,145,145,-103,-103,-74,-75,145,]),'CARACTERVAL':([98,101,102,104,114,115,116,117,118,119,120,121,137,139,141,142,175,178,179,180,184,185,205,206,219,220,223,225,226,227,228,229,230,239,254,255,256,257,258,259,264,268,270,271,278,279,282,],[146,146,146,146,146,146,146,146,146,146,146,146,146,146,-103,-103,146,146,-103,-103,-70,-71,146,146,-72,-73,146,-103,-103,-103,-103,-103,-103,146,-76,-77,-78,-79,-80,-81,146,146,-103,-103,-74,-75,146,]),'LETRERO':([102,],[154,]),'MULT':([133,136,138,140,143,144,145,146,171,183,186,187,188,189,221,251,],[-103,179,-89,-91,-103,-103,-103,-103,-93,-90,-92,-94,-95,-96,-103,-88,]),'DIV':([133,136,138,140,143,144,145,146,171,183,186,187,188,189,221,251,],[-103,180,-89,-91,-103,-103,-103,-103,-93,-90,-92,-94,-95,-96,-103,-88,]),'MENORQUE':([133,135,136,138,140,143,144,145,146,171,173,174,176,177,182,183,186,187,188,189,215,216,217,218,221,249,250,251,],[-103,-103,-103,-89,-91,-103,-103,-103,-103,-93,-103,-84,-103,-87,225,-90,-92,-94,-95,-96,-82,-103,-85,-103,-103,-83,-86,-88,]),'MAYORQUE':([133,135,136,138,140,143,144,145,146,171,173,174,176,177,182,183,186,187,188,189,215,216,217,218,221,249,250,251,],[-103,-103,-103,-89,-91,-103,-103,-103,-103,-93,-103,-84,-103,-87,226,-90,-92,-94,-95,-96,-82,-103,-85,-103,-103,-83,-86,-88,]),'MENORIGUALQUE':([133,135,136,138,140,143,144,145,146,171,173,174,176,177,182,183,186,187,188,189,215,216,217,218,221,249,250,251,],[-103,-103,-103,-89,-91,-103,-103,-103,-103,-93,-103,-84,-103,-87,227,-90,-92,-94,-95,-96,-82,-103,-85,-103,-103,-83,-86,-88,]),'MAYORIGUALQUE':([133,135,136,138,140,143,144,145,146,171,173,174,176,177,182,183,186,187,188,189,215,216,217,218,221,249,250,251,],[-103,-103,-103,-89,-91,-103,-103,-103,-103,-93,-103,-84,-103,-87,228,-90,-92,-94,-95,-96,-82,-103,-85,-103,-103,-83,-86,-88,]),'IGUALQUE':([133,135,136,138,140,143,144,145,146,171,173,174,176,177,182,183,186,187,188,189,215,216,217,218,221,249,250,251,],[-103,-103,-103,-89,-91,-103,-103,-103,-103,-93,-103,-84,-103,-87,229,-90,-92,-94,-95,-96,-82,-103,-85,-103,-103,-83,-86,-88,]),'DIFQUE':([133,135,136,138,140,143,144,145,146,171,173,174,176,177,182,183,186,187,188,189,215,216,217,218,221,249,250,251,],[-103,-103,-103,-89,-91,-103,-103,-103,-103,-93,-103,-84,-103,-87,230,-90,-92,-94,-95,-96,-82,-103,-85,-103,-103,-83,-86,-88,]),'OR':([133,135,136,138,140,143,144,145,146,171,173,174,176,177,183,186,187,188,189,215,216,217,218,221,249,250,251,253,],[-103,-103,-103,-89,-91,-103,-103,-103,-103,-93,-103,-84,-103,-87,-90,-92,-94,-95,-96,-82,-103,-85,-103,-103,-83,-86,-88,270,]),'AND':([133,135,136,138,140,143,144,145,146,171,173,174,176,177,183,186,187,188,189,215,216,217,218,221,249,250,251,253,],[-103,-103,-103,-89,-91,-103,-103,-103,-103,-93,-103,-84,-103,-87,-90,-92,-94,-95,-96,-82,-103,-85,-103,-103,-83,-86,-88,271,]),'HACER':([133,135,136,138,140,143,144,145,146,171,173,174,176,177,183,186,187,188,189,200,215,216,217,218,221,249,250,251,263,],[-103,-103,-103,-89,-91,-103,-103,-103,-103,-93,-103,-84,-103,-87,-90,-92,-94,-95,-96,238,-82,-103,-85,-103,-103,-83,-86,-88,274,]),'ENTONCES':([155,],[199,]),'HASTA':([201,],[239,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'variables':([4,84,],[5,123,]),'empty':([4,5,7,12,13,14,15,32,33,34,36,37,41,42,50,56,57,58,67,68,69,70,71,72,73,74,84,85,86,88,89,90,91,92,93,97,99,122,133,134,135,136,141,142,143,144,145,146,147,153,154,167,169,170,173,176,179,180,182,190,192,193,194,195,196,202,203,204,207,208,209,211,216,218,221,225,226,227,228,229,230,232,252,253,262,265,270,271,272,277,281,286,],[6,9,18,22,23,24,25,38,39,40,45,18,47,49,87,94,95,96,106,107,108,109,110,111,112,113,6,124,125,126,127,128,129,130,131,132,149,168,171,172,174,177,184,185,186,187,188,189,191,197,198,210,45,214,215,217,219,220,224,231,149,233,234,235,236,240,241,242,245,246,247,248,249,250,251,254,255,256,257,258,259,260,266,269,273,276,278,279,280,283,284,287,]),'funciones':([5,170,],[8,213,]),'funcionesU':([5,170,],[10,10,]),'tipo_funcion':([5,170,],[11,11,]),'variablesU':([7,37,],[16,46,]),'variablesD':([7,26,37,],[17,30,17,]),'tipo_var':([27,83,],[31,122,]),'bloque':([35,123,199,238,261,274,],[41,170,237,262,272,281,]),'recibir_parametros':([36,169,],[44,211,]),'bloqueU':([42,50,],[48,88,]),'estatuto':([42,50,],[50,50,]),'asignacion':([42,50,105,],[51,51,157,]),'llamada':([42,50,],[52,52,]),'retorno':([42,50,],[53,53,]),'lectura':([42,50,],[54,54,]),'escritura':([42,50,],[55,55,]),'decision':([42,50,],[56,56,]),'condicional':([42,50,],[57,57,]),'no_condicional':([42,50,],[58,58,]),'funciones_especiales':([42,50,],[59,59,]),'circulo':([42,50,],[67,67,]),'color':([42,50,],[68,68,]),'grosor':([42,50,],[69,69,]),'linea':([42,50,],[70,70,]),'puntoxy':([42,50,],[71,71,]),'arco':([42,50,],[72,72,]),'penup':([42,50,],[73,73,]),'pendown':([42,50,],[74,74,]),'bloqueD':([50,],[86,]),'exp':([98,101,102,104,114,115,116,117,118,119,120,121,137,175,205,206,223,239,264,268,282,],[134,151,153,156,159,160,161,162,163,164,165,166,182,216,243,244,253,263,275,277,285,]),'termino':([98,101,102,104,114,115,116,117,118,119,120,121,137,175,178,205,206,223,239,264,268,282,],[135,135,135,135,135,135,135,135,135,135,135,135,135,135,218,135,135,135,135,135,135,135,]),'factor':([98,101,102,104,114,115,116,117,118,119,120,121,137,175,178,205,206,223,239,264,268,282,],[136,136,136,136,136,136,136,136,136,136,136,136,136,136,136,136,136,136,136,136,136,136,]),'factorU':([98,101,102,104,114,115,116,117,118,119,120,121,137,175,178,205,206,223,239,264,268,282,],[138,138,138,138,138,138,138,138,138,138,138,138,138,138,138,138,138,138,138,138,138,138,]),'operadorA':([98,101,102,104,114,115,116,117,118,119,120,121,135,137,175,178,205,206,223,239,264,268,282,],[139,139,139,139,139,139,139,139,139,139,139,139,175,139,139,139,139,139,139,139,139,139,139,]),'factorD':([98,101,102,104,114,115,116,117,118,119,120,121,137,139,175,178,205,206,223,239,264,268,282,],[140,140,140,140,140,140,140,140,140,140,140,140,140,183,140,140,140,140,140,140,140,140,140,]),'varcte':([98,101,102,104,114,115,116,117,118,119,120,121,137,139,175,178,205,206,223,239,264,268,282,],[143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,]),'mandar_parametros':([99,192,],[148,232,]),'escrituraD':([102,],[152,]),'recibir_parametrosD':([122,],[167,]),'expU':([135,],[173,]),'terminoU':([136,],[176,]),'operadorT':([136,],[178,]),'expresion':([137,],[181,]),'mandar_parametrosD':([147,],[190,]),'funcionesD':([170,],[212,]),'expresionU':([182,],[222,]),'operadorR':([182,],[223,]),'expresion_dos':([223,],[252,]),'expresion_dosU':([253,],[267,]),'operadorL':([253,],[268,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAMA ID PUNTOYCOMA variables funciones PRINCIPAL L_PAR R_PAR bloque empty','program',10,'p_programa','lexer_parser.py',211),
  ('variables -> VARIABLES variablesU','variables',2,'p_variales','lexer_parser.py',216),
  ('variables -> empty','variables',1,'p_variales','lexer_parser.py',217),
  ('variablesU -> variablesD','variablesU',1,'p_variales','lexer_parser.py',219),
  ('variablesU -> empty','variablesU',1,'p_variales','lexer_parser.py',220),
  ('variablesD -> ID COMA variablesD','variablesD',3,'p_variales','lexer_parser.py',222),
  ('variablesD -> ID DOSPUNTOS tipo_var PUNTOYCOMA variablesU','variablesD',5,'p_variales','lexer_parser.py',223),
  ('funciones -> funcionesU','funciones',1,'p_funciones','lexer_parser.py',228),
  ('funciones -> empty','funciones',1,'p_funciones','lexer_parser.py',229),
  ('funcionesU -> tipo_funcion FUNCION ID L_PAR recibir_parametros R_PAR variables bloque funcionesD','funcionesU',9,'p_funciones','lexer_parser.py',231),
  ('funcionesD -> funciones','funcionesD',1,'p_funciones','lexer_parser.py',233),
  ('funcionesD -> empty','funcionesD',1,'p_funciones','lexer_parser.py',234),
  ('tipo_funcion -> ENTERO empty','tipo_funcion',2,'p_tipo_funcion','lexer_parser.py',239),
  ('tipo_funcion -> FLOTANTE empty','tipo_funcion',2,'p_tipo_funcion','lexer_parser.py',240),
  ('tipo_funcion -> CARACTER empty','tipo_funcion',2,'p_tipo_funcion','lexer_parser.py',241),
  ('tipo_funcion -> VOID empty','tipo_funcion',2,'p_tipo_funcion','lexer_parser.py',242),
  ('tipo_var -> ENTERO empty','tipo_var',2,'p_tipo_var','lexer_parser.py',247),
  ('tipo_var -> FLOTANTE empty','tipo_var',2,'p_tipo_var','lexer_parser.py',248),
  ('tipo_var -> CARACTER empty','tipo_var',2,'p_tipo_var','lexer_parser.py',249),
  ('recibir_parametros -> ID DOSPUNTOS tipo_var recibir_parametrosD empty','recibir_parametros',5,'p_recibir_parametros','lexer_parser.py',254),
  ('recibir_parametros -> empty','recibir_parametros',1,'p_recibir_parametros','lexer_parser.py',255),
  ('recibir_parametrosD -> COMA recibir_parametros empty','recibir_parametrosD',3,'p_recibir_parametros','lexer_parser.py',257),
  ('recibir_parametrosD -> empty','recibir_parametrosD',1,'p_recibir_parametros','lexer_parser.py',258),
  ('mandar_parametros -> ID mandar_parametrosD empty','mandar_parametros',3,'p_mandar_parametros','lexer_parser.py',263),
  ('mandar_parametros -> empty','mandar_parametros',1,'p_mandar_parametros','lexer_parser.py',264),
  ('mandar_parametrosD -> COMA mandar_parametros empty','mandar_parametrosD',3,'p_mandar_parametros','lexer_parser.py',266),
  ('mandar_parametrosD -> empty','mandar_parametrosD',1,'p_mandar_parametros','lexer_parser.py',267),
  ('bloque -> L_LLAVE bloqueU R_LLAVE empty','bloque',4,'p_bloque','lexer_parser.py',274),
  ('bloqueU -> estatuto bloqueD empty','bloqueU',3,'p_bloque','lexer_parser.py',276),
  ('bloqueU -> empty','bloqueU',1,'p_bloque','lexer_parser.py',277),
  ('bloqueD -> bloqueU empty','bloqueD',2,'p_bloque','lexer_parser.py',279),
  ('bloqueD -> empty','bloqueD',1,'p_bloque','lexer_parser.py',280),
  ('estatuto -> asignacion PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',285),
  ('estatuto -> llamada PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',286),
  ('estatuto -> retorno PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',287),
  ('estatuto -> lectura PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',288),
  ('estatuto -> escritura PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',289),
  ('estatuto -> decision empty','estatuto',2,'p_estatuto','lexer_parser.py',290),
  ('estatuto -> condicional empty','estatuto',2,'p_estatuto','lexer_parser.py',291),
  ('estatuto -> no_condicional empty','estatuto',2,'p_estatuto','lexer_parser.py',292),
  ('estatuto -> funciones_especiales PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',293),
  ('estatuto -> empty','estatuto',1,'p_estatuto','lexer_parser.py',294),
  ('asignacion -> ID IGUAL exp empty','asignacion',4,'p_asignacion','lexer_parser.py',299),
  ('llamada -> ID L_PAR mandar_parametros R_PAR empty','llamada',5,'p_llamada','lexer_parser.py',304),
  ('retorno -> REGRESA L_PAR ID R_PAR empty','retorno',5,'p_retorno','lexer_parser.py',309),
  ('lectura -> LEER L_PAR exp R_PAR empty','lectura',5,'p_lectura','lexer_parser.py',314),
  ('escritura -> ESCRIBIR L_PAR escrituraD R_PAR empty','escritura',5,'p_escritura','lexer_parser.py',319),
  ('escrituraD -> exp empty','escrituraD',2,'p_escritura','lexer_parser.py',321),
  ('escrituraD -> LETRERO empty','escrituraD',2,'p_escritura','lexer_parser.py',322),
  ('decision -> SI L_PAR R_PAR ENTONCES bloque SINO bloque empty','decision',8,'p_decision','lexer_parser.py',327),
  ('condicional -> MIENTRAS L_PAR exp R_PAR HACER bloque empty','condicional',7,'p_condicional','lexer_parser.py',332),
  ('no_condicional -> DESDE L_PAR asignacion R_PAR HASTA exp HACER bloque empty','no_condicional',9,'p_no_condicional','lexer_parser.py',337),
  ('funciones_especiales -> circulo empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',344),
  ('funciones_especiales -> color empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',345),
  ('funciones_especiales -> grosor empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',346),
  ('funciones_especiales -> linea empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',347),
  ('funciones_especiales -> puntoxy empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',348),
  ('funciones_especiales -> arco empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',349),
  ('funciones_especiales -> penup empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',350),
  ('funciones_especiales -> pendown empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',351),
  ('funciones_especiales -> empty','funciones_especiales',1,'p_funciones_especiales','lexer_parser.py',352),
  ('circulo -> CIRCULO L_PAR exp R_PAR empty','circulo',5,'p_circulo','lexer_parser.py',357),
  ('color -> COLOR L_PAR exp R_PAR empty','color',5,'p_color','lexer_parser.py',362),
  ('grosor -> GROSOR L_PAR exp R_PAR empty','grosor',5,'p_grosor','lexer_parser.py',367),
  ('linea -> LINEA L_PAR exp COMA exp COMA exp COMA exp R_PAR empty','linea',11,'p_linea','lexer_parser.py',372),
  ('puntoxy -> PUNTOXY L_PAR exp COMA exp R_PAR empty','puntoxy',7,'p_puntoxy','lexer_parser.py',377),
  ('arco -> ARCO L_PAR exp R_PAR empty','arco',5,'p_arco','lexer_parser.py',382),
  ('penup -> PENUP L_PAR exp R_PAR empty','penup',5,'p_penup','lexer_parser.py',387),
  ('pendown -> PENDOWN L_PAR exp R_PAR empty','pendown',5,'p_pendown','lexer_parser.py',392),
  ('operadorA -> MAS empty','operadorA',2,'p_operadorA','lexer_parser.py',399),
  ('operadorA -> MENOS empty','operadorA',2,'p_operadorA','lexer_parser.py',400),
  ('operadorT -> MULT empty','operadorT',2,'p_operadorT','lexer_parser.py',405),
  ('operadorT -> DIV empty','operadorT',2,'p_operadorT','lexer_parser.py',406),
  ('operadorL -> OR empty','operadorL',2,'p_operadorL','lexer_parser.py',411),
  ('operadorL -> AND empty','operadorL',2,'p_operadorL','lexer_parser.py',412),
  ('operadorR -> MENORQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',417),
  ('operadorR -> MAYORQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',418),
  ('operadorR -> MENORIGUALQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',419),
  ('operadorR -> MAYORIGUALQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',420),
  ('operadorR -> IGUALQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',421),
  ('operadorR -> DIFQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',422),
  ('exp -> termino expU empty','exp',3,'p_exp','lexer_parser.py',429),
  ('expU -> operadorA exp empty','expU',3,'p_exp','lexer_parser.py',431),
  ('expU -> empty','expU',1,'p_exp','lexer_parser.py',432),
  ('termino -> factor terminoU empty','termino',3,'p_termino','lexer_parser.py',437),
  ('terminoU -> operadorT termino empty','terminoU',3,'p_termino','lexer_parser.py',439),
  ('terminoU -> empty','terminoU',1,'p_termino','lexer_parser.py',440),
  ('factor -> L_PAR expresion R_PAR empty','factor',4,'p_factor','lexer_parser.py',445),
  ('factor -> factorU','factor',1,'p_factor','lexer_parser.py',446),
  ('factorU -> operadorA factorD','factorU',2,'p_factor','lexer_parser.py',448),
  ('factorU -> factorD','factorU',1,'p_factor','lexer_parser.py',449),
  ('factorD -> varcte empty','factorD',2,'p_factor','lexer_parser.py',451),
  ('varcte -> ID empty','varcte',2,'p_varcte','lexer_parser.py',456),
  ('varcte -> ENTEROVAL empty','varcte',2,'p_varcte','lexer_parser.py',457),
  ('varcte -> FLOTANTEVAL empty','varcte',2,'p_varcte','lexer_parser.py',458),
  ('varcte -> CARACTERVAL empty','varcte',2,'p_varcte','lexer_parser.py',459),
  ('expresion -> exp expresionU','expresion',2,'p_expresion','lexer_parser.py',464),
  ('expresionU -> operadorR expresion_dos empty','expresionU',3,'p_expresion','lexer_parser.py',466),
  ('expresionU -> empty','expresionU',1,'p_expresion','lexer_parser.py',467),
  ('expresion_dos -> exp expresion_dosU','expresion_dos',2,'p_expresion_dos','lexer_parser.py',472),
  ('expresion_dosU -> operadorL exp empty','expresion_dosU',3,'p_expresion_dos','lexer_parser.py',474),
  ('expresion_dosU -> empty','expresion_dosU',1,'p_expresion_dos','lexer_parser.py',475),
  ('empty -> <empty>','empty',0,'p_empty','lexer_parser.py',485),
]
