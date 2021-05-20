
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARCO CARACTER CARACTERVAL CIRCULO COLOR COMA DESDE DIFQUE DIV DOSPUNTOS ENTERO ENTEROVAL ENTONCES ESCRIBIR FLOTANTE FLOTANTEVAL FUNCION GROSOR HACER HASTA ID IGUAL IGUALQUE LEER LETRERO LINEA L_CORCHETE L_LLAVE L_PAR MAS MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MENOS MIENTRAS MULT OR PENDOWN PENUP PRINCIPAL PROGRAMA PUNTO PUNTOXY PUNTOYCOMA REGRESA R_CORCHETE R_LLAVE R_PAR SI SINO VARIABLES VOID\n    program : PROGRAMA ID neu_programa PUNTOYCOMA variables funciones PRINCIPAL L_PAR R_PAR bloque empty\n    \n    variables : VARIABLES variablesU\n              | empty\n\n    variablesU : variablesD\n               | empty\n\n    variablesD : ID neu_addVariableAStack COMA variablesD\n               | ID DOSPUNTOS tipo_var neu_addVariable PUNTOYCOMA variablesU\n    \n    funciones : funcionesU\n              | empty\n    \n    funcionesU : tipo_funcion FUNCION ID neu_addFuncion L_PAR recibir_parametros R_PAR variables bloque funcionesD\n    \n    funcionesD : funciones\n               | empty\n    \n    tipo_funcion : ENTERO empty\n                 | FLOTANTE empty\n                 | CARACTER empty\n                 | VOID empty\n    \n    tipo_var : ENTERO empty\n             | FLOTANTE empty\n             | CARACTER empty\n    \n    recibir_parametros : ID DOSPUNTOS tipo_var recibir_parametrosD empty\n                       | empty\n\n    recibir_parametrosD : COMA recibir_parametros empty\n                       | empty\n    \n    mandar_parametros : ID mandar_parametrosD empty\n                      | empty\n\n    mandar_parametrosD : COMA mandar_parametros empty\n                       | empty\n    \n    bloque : L_LLAVE bloqueU R_LLAVE empty\n\n    bloqueU : estatuto bloqueD empty\n            | empty\n\n    bloqueD : bloqueU empty\n            | empty\n    \n    estatuto : asignacion PUNTOYCOMA empty\n             | llamada PUNTOYCOMA empty\n             | retorno PUNTOYCOMA empty\n             | lectura PUNTOYCOMA empty\n             | escritura PUNTOYCOMA empty\n             | decision empty\n             | condicional empty\n             | no_condicional empty\n             | funciones_especiales PUNTOYCOMA empty\n             | empty\n    \n    asignacion : ID IGUAL hiper_exp empty\n    \n    llamada : ID L_PAR mandar_parametros R_PAR neu_llamada empty\n    \n    retorno : REGRESA L_PAR ID R_PAR empty\n    \n    lectura : LEER L_PAR ID R_PAR empty\n    \n    escritura : ESCRIBIR L_PAR escrituraD R_PAR empty\n\n    escrituraD : hiper_exp empty\n               | LETRERO empty\n    \n    decision : SI L_PAR hiper_exp R_PAR ENTONCES bloque decisionU empty\n\n    decisionU : SINO bloque empty\n              | empty\n    \n    condicional : MIENTRAS L_PAR hiper_exp R_PAR HACER bloque empty\n    \n    no_condicional : DESDE L_PAR asignacion R_PAR HASTA hiper_exp HACER bloque empty\n    \n    funciones_especiales : circulo empty\n                         | color empty\n                         | grosor empty\n                         | linea empty\n                         | puntoxy empty\n                         | arco empty\n                         | penup empty\n                         | pendown empty\n                         | empty\n    \n    circulo : CIRCULO L_PAR hiper_exp R_PAR empty\n    \n    color : COLOR L_PAR hiper_exp R_PAR empty\n    \n    grosor : GROSOR L_PAR hiper_exp R_PAR empty\n    \n    linea : LINEA L_PAR hiper_exp COMA hiper_exp COMA hiper_exp COMA hiper_exp R_PAR empty\n    \n    puntoxy : PUNTOXY L_PAR hiper_exp COMA hiper_exp R_PAR empty\n    \n    arco : ARCO L_PAR hiper_exp R_PAR empty\n    \n    penup : PENUP L_PAR hiper_exp R_PAR empty\n    \n    pendown : PENDOWN L_PAR hiper_exp R_PAR empty\n    \n    operadorA : MAS empty\n              | MENOS empty\n    \n    operadorT : MULT empty\n              | DIV empty\n    \n    operadorL : OR empty\n              | AND empty\n    \n    operadorR : MENORQUE empty\n              | MAYORQUE empty\n              | MENORIGUALQUE empty\n              | MAYORIGUALQUE empty\n              | IGUALQUE empty\n              | DIFQUE empty\n    \n    hiper_exp : super_exp hiper_expU\n\n    hiper_expU : operadorL hiper_exp empty \n               | empty\n    \n    super_exp : exp super_expU\n\n    super_expU : operadorR exp empty \n               | empty\n    \n    exp : termino expU\n\n    expU : operadorA exp\n         | empty\n    \n    termino : factor terminoU\n\n    terminoU : operadorT termino\n             | empty\n    \n    factor : varcte empty\n           | llamada empty\n           | L_PAR hiper_exp R_PAR empty\n    \n    varcte  : ID empty\n            | ENTEROVAL empty\n            | FLOTANTEVAL empty\n            | CARACTERVAL empty\n    \n    empty : \n    neu_programa : neu_addFuncion : neu_addVariable : neu_addVariableAStack : neu_llamada : '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,43,47,87,126,],[0,-103,-1,-103,-28,]),'ID':([2,8,22,31,44,45,46,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,116,117,118,119,120,121,122,123,126,129,130,131,132,133,134,143,172,174,175,177,179,180,181,182,183,184,186,188,189,191,193,194,203,216,217,223,226,227,229,230,231,232,233,234,236,237,239,240,250,269,270,272,275,276,278,282,283,284,285,286,287,],[3,20,30,20,60,83,20,-42,60,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,135,147,150,151,135,135,135,158,135,135,135,135,135,135,135,135,-28,-33,-34,-35,-36,-37,-41,135,135,-103,-103,135,-103,-103,-103,-103,-103,-103,135,-103,-103,135,-103,-103,147,135,135,83,-76,-77,-78,-79,-80,-81,-82,-83,-72,-73,-74,-75,135,-103,-103,135,-103,-52,-53,-50,-103,-103,135,-51,-54,]),'PUNTOYCOMA':([3,4,32,33,34,35,39,40,41,42,44,49,50,51,52,53,54,55,56,57,58,59,67,68,69,70,71,72,73,74,87,89,91,92,93,94,95,96,97,98,99,108,109,110,111,112,113,114,115,126,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,169,170,171,173,176,178,185,187,190,192,195,196,198,199,200,204,205,206,207,213,214,215,218,219,220,225,228,235,238,241,244,245,246,247,251,252,253,256,257,258,264,265,266,268,269,270,273,275,276,278,281,282,283,284,286,287,289,290,],[-104,5,-106,-103,-103,-103,46,-17,-18,-19,-103,-42,-103,91,92,93,94,95,-103,-103,-103,99,-103,-103,-103,-103,-103,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-55,-56,-57,-58,-59,-60,-61,-62,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-99,-43,-84,-86,-87,-89,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-91,-94,-103,-103,-45,-46,-47,-64,-65,-66,-69,-70,-71,-85,-88,-98,-44,-103,-103,-103,-103,-52,-53,-68,-50,-103,-103,-51,-54,-103,-67,]),'VARIABLES':([5,125,],[8,8,]),'ENTERO':([5,6,7,8,17,18,19,28,38,46,86,87,124,126,224,],[-103,13,-3,-103,-2,-4,-5,33,-6,-103,-7,-103,33,-28,13,]),'FLOTANTE':([5,6,7,8,17,18,19,28,38,46,86,87,124,126,224,],[-103,14,-3,-103,-2,-4,-5,34,-6,-103,-7,-103,34,-28,14,]),'CARACTER':([5,6,7,8,17,18,19,28,38,46,86,87,124,126,224,],[-103,15,-3,-103,-2,-4,-5,35,-6,-103,-7,-103,35,-28,15,]),'VOID':([5,6,7,8,17,18,19,38,46,86,87,126,224,],[-103,16,-3,-103,-2,-4,-5,-6,-103,-7,-103,-28,16,]),'PRINCIPAL':([5,6,7,8,9,10,11,17,18,19,38,46,86,87,126,224,261,262,263,],[-103,-103,-3,-103,21,-9,-8,-2,-4,-5,-6,-103,-7,-103,-28,-103,-10,-11,-9,]),'L_LLAVE':([7,8,17,18,19,36,38,46,86,125,168,248,249,277,279,],[-3,-103,-2,-4,-5,44,-6,-103,-7,-103,44,44,44,44,44,]),'FUNCION':([12,13,14,15,16,23,24,25,26,],[22,-103,-103,-103,-103,-13,-14,-15,-16,]),'DOSPUNTOS':([20,83,],[28,124,]),'COMA':([20,27,33,34,35,40,41,42,135,137,138,139,140,141,142,144,145,146,147,162,163,167,169,171,173,176,178,185,187,190,192,195,196,198,199,200,204,225,228,235,238,241,244,254,264,265,266,268,280,],[-107,31,-103,-103,-103,-17,-18,-19,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,203,216,217,223,-99,-84,-86,-87,-89,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,-103,-103,-91,-94,-103,-103,272,-85,-88,-98,-44,285,]),'L_PAR':([21,30,37,60,61,62,63,64,65,66,75,76,77,78,79,80,81,82,100,104,105,106,116,117,118,119,120,121,122,123,135,143,172,174,175,177,179,180,181,182,183,184,186,188,189,191,193,194,216,217,226,227,229,230,231,232,233,234,236,237,239,240,250,272,285,],[29,-105,45,101,102,103,104,105,106,107,116,117,118,119,120,121,122,123,143,143,143,143,143,143,143,143,143,143,143,143,101,143,143,-103,-103,143,-103,-103,-103,-103,-103,-103,143,-103,-103,143,-103,-103,143,143,-76,-77,-78,-79,-80,-81,-82,-83,-72,-73,-74,-75,143,143,143,]),'R_PAR':([29,33,34,35,40,41,42,45,84,85,101,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,164,165,166,167,169,170,171,173,176,178,185,187,190,192,195,196,197,198,199,200,201,202,203,204,208,209,221,222,223,225,228,235,238,241,242,243,244,255,259,260,264,265,266,267,268,274,288,],[36,-103,-103,-103,-17,-18,-19,-103,125,-21,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,204,-25,205,206,207,-103,-103,210,211,212,213,214,215,218,219,220,-103,-99,-43,-84,-86,-87,-89,-90,-92,-93,-95,-96,-97,241,-100,-101,-102,-103,-27,-103,-108,-48,-49,-103,-23,-103,-103,-103,-91,-94,-103,-24,-103,-103,273,-20,-103,-85,-88,-98,-26,-44,-22,289,]),'R_LLAVE':([44,48,49,50,56,57,58,87,88,89,90,91,92,93,94,95,96,97,98,99,126,127,128,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[-103,87,-30,-103,-103,-103,-103,-103,-103,-30,-103,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-29,-31,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'REGRESA':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[61,-42,61,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'LEER':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[62,-42,62,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'ESCRIBIR':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[63,-42,63,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'SI':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[64,-42,64,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'MIENTRAS':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[65,-42,65,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'DESDE':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[66,-42,66,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'CIRCULO':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[75,-42,75,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'COLOR':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[76,-42,76,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'GROSOR':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[77,-42,77,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'LINEA':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[78,-42,78,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'PUNTOXY':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[79,-42,79,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'ARCO':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[80,-42,80,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'PENUP':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[81,-42,81,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'PENDOWN':([44,49,50,56,57,58,87,89,91,92,93,94,95,96,97,98,99,126,129,130,131,132,133,134,269,270,275,276,278,282,283,284,286,287,],[82,-42,82,-103,-103,-103,-103,-42,-103,-103,-103,-103,-103,-38,-39,-40,-103,-28,-33,-34,-35,-36,-37,-41,-103,-103,-103,-52,-53,-50,-103,-103,-51,-54,]),'IGUAL':([60,158,],[100,100,]),'SINO':([87,126,269,],[-103,-28,277,]),'ENTEROVAL':([100,104,105,106,116,117,118,119,120,121,122,123,143,172,174,175,177,179,180,181,182,183,184,186,188,189,191,193,194,216,217,226,227,229,230,231,232,233,234,236,237,239,240,250,272,285,],[144,144,144,144,144,144,144,144,144,144,144,144,144,144,-103,-103,144,-103,-103,-103,-103,-103,-103,144,-103,-103,144,-103,-103,144,144,-76,-77,-78,-79,-80,-81,-82,-83,-72,-73,-74,-75,144,144,144,]),'FLOTANTEVAL':([100,104,105,106,116,117,118,119,120,121,122,123,143,172,174,175,177,179,180,181,182,183,184,186,188,189,191,193,194,216,217,226,227,229,230,231,232,233,234,236,237,239,240,250,272,285,],[145,145,145,145,145,145,145,145,145,145,145,145,145,145,-103,-103,145,-103,-103,-103,-103,-103,-103,145,-103,-103,145,-103,-103,145,145,-76,-77,-78,-79,-80,-81,-82,-83,-72,-73,-74,-75,145,145,145,]),'CARACTERVAL':([100,104,105,106,116,117,118,119,120,121,122,123,143,172,174,175,177,179,180,181,182,183,184,186,188,189,191,193,194,216,217,226,227,229,230,231,232,233,234,236,237,239,240,250,272,285,],[146,146,146,146,146,146,146,146,146,146,146,146,146,146,-103,-103,146,-103,-103,-103,-103,-103,-103,146,-103,-103,146,-103,-103,146,146,-76,-77,-78,-79,-80,-81,-82,-83,-72,-73,-74,-75,146,146,146,]),'LETRERO':([104,],[154,]),'MULT':([135,140,141,142,144,145,146,169,195,196,198,199,200,204,241,244,266,268,],[-103,193,-103,-103,-103,-103,-103,-99,-96,-97,-100,-101,-102,-108,-103,-103,-98,-44,]),'DIV':([135,140,141,142,144,145,146,169,195,196,198,199,200,204,241,244,266,268,],[-103,194,-103,-103,-103,-103,-103,-99,-96,-97,-100,-101,-102,-108,-103,-103,-98,-44,]),'MAS':([135,139,140,141,142,144,145,146,169,190,192,195,196,198,199,200,204,238,241,244,266,268,],[-103,188,-103,-103,-103,-103,-103,-103,-99,-93,-95,-96,-97,-100,-101,-102,-108,-94,-103,-103,-98,-44,]),'MENOS':([135,139,140,141,142,144,145,146,169,190,192,195,196,198,199,200,204,238,241,244,266,268,],[-103,189,-103,-103,-103,-103,-103,-103,-99,-93,-95,-96,-97,-100,-101,-102,-108,-94,-103,-103,-98,-44,]),'MENORQUE':([135,138,139,140,141,142,144,145,146,169,185,187,190,192,195,196,198,199,200,204,235,238,241,244,266,268,],[-103,179,-103,-103,-103,-103,-103,-103,-103,-99,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,-91,-94,-103,-103,-98,-44,]),'MAYORQUE':([135,138,139,140,141,142,144,145,146,169,185,187,190,192,195,196,198,199,200,204,235,238,241,244,266,268,],[-103,180,-103,-103,-103,-103,-103,-103,-103,-99,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,-91,-94,-103,-103,-98,-44,]),'MENORIGUALQUE':([135,138,139,140,141,142,144,145,146,169,185,187,190,192,195,196,198,199,200,204,235,238,241,244,266,268,],[-103,181,-103,-103,-103,-103,-103,-103,-103,-99,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,-91,-94,-103,-103,-98,-44,]),'MAYORIGUALQUE':([135,138,139,140,141,142,144,145,146,169,185,187,190,192,195,196,198,199,200,204,235,238,241,244,266,268,],[-103,182,-103,-103,-103,-103,-103,-103,-103,-99,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,-91,-94,-103,-103,-98,-44,]),'IGUALQUE':([135,138,139,140,141,142,144,145,146,169,185,187,190,192,195,196,198,199,200,204,235,238,241,244,266,268,],[-103,183,-103,-103,-103,-103,-103,-103,-103,-99,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,-91,-94,-103,-103,-98,-44,]),'DIFQUE':([135,138,139,140,141,142,144,145,146,169,185,187,190,192,195,196,198,199,200,204,235,238,241,244,266,268,],[-103,184,-103,-103,-103,-103,-103,-103,-103,-99,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,-91,-94,-103,-103,-98,-44,]),'OR':([135,137,138,139,140,141,142,144,145,146,169,176,178,185,187,190,192,195,196,198,199,200,204,228,235,238,241,244,265,266,268,],[-103,174,-103,-103,-103,-103,-103,-103,-103,-103,-99,-87,-89,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,-103,-91,-94,-103,-103,-88,-98,-44,]),'AND':([135,137,138,139,140,141,142,144,145,146,169,176,178,185,187,190,192,195,196,198,199,200,204,228,235,238,241,244,265,266,268,],[-103,175,-103,-103,-103,-103,-103,-103,-103,-103,-99,-87,-89,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,-103,-91,-94,-103,-103,-88,-98,-44,]),'HACER':([135,137,138,139,140,141,142,144,145,146,169,171,173,176,178,185,187,190,192,195,196,198,199,200,204,211,225,228,235,238,241,244,264,265,266,268,271,],[-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-99,-84,-86,-87,-89,-90,-92,-93,-95,-96,-97,-100,-101,-102,-108,249,-103,-103,-91,-94,-103,-103,-85,-88,-98,-44,279,]),'ENTONCES':([210,],[248,]),'HASTA':([212,],[250,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'neu_programa':([3,],[4,]),'variables':([5,125,],[6,168,]),'empty':([5,6,8,13,14,15,16,33,34,35,43,44,45,46,50,56,57,58,67,68,69,70,71,72,73,74,87,88,90,91,92,93,94,95,99,101,125,135,136,137,138,139,140,141,142,144,145,146,147,153,154,167,174,175,179,180,181,182,183,184,188,189,193,194,201,203,205,206,207,213,214,215,218,219,220,221,223,224,225,228,241,243,244,260,269,270,273,275,283,284,289,],[7,10,19,23,24,25,26,40,41,42,47,49,85,19,89,96,97,98,108,109,110,111,112,113,114,115,126,127,128,129,130,131,132,133,134,149,7,169,170,173,178,187,192,195,196,198,199,200,202,208,209,222,226,227,229,230,231,232,233,234,236,237,239,240,242,149,245,246,247,251,252,253,256,257,258,259,85,263,264,265,266,267,268,274,276,278,281,282,286,287,290,]),'funciones':([6,224,],[9,262,]),'funcionesU':([6,224,],[11,11,]),'tipo_funcion':([6,224,],[12,12,]),'variablesU':([8,46,],[17,86,]),'variablesD':([8,31,46,],[18,38,18,]),'neu_addVariableAStack':([20,],[27,]),'tipo_var':([28,124,],[32,167,]),'neu_addFuncion':([30,],[37,]),'neu_addVariable':([32,],[39,]),'bloque':([36,168,248,249,277,279,],[43,224,269,270,283,284,]),'bloqueU':([44,50,],[48,90,]),'estatuto':([44,50,],[50,50,]),'asignacion':([44,50,107,],[51,51,157,]),'llamada':([44,50,100,104,105,106,116,117,118,119,120,121,122,123,143,172,177,186,191,216,217,250,272,285,],[52,52,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,]),'retorno':([44,50,],[53,53,]),'lectura':([44,50,],[54,54,]),'escritura':([44,50,],[55,55,]),'decision':([44,50,],[56,56,]),'condicional':([44,50,],[57,57,]),'no_condicional':([44,50,],[58,58,]),'funciones_especiales':([44,50,],[59,59,]),'circulo':([44,50,],[67,67,]),'color':([44,50,],[68,68,]),'grosor':([44,50,],[69,69,]),'linea':([44,50,],[70,70,]),'puntoxy':([44,50,],[71,71,]),'arco':([44,50,],[72,72,]),'penup':([44,50,],[73,73,]),'pendown':([44,50,],[74,74,]),'recibir_parametros':([45,223,],[84,260,]),'bloqueD':([50,],[88,]),'hiper_exp':([100,104,105,106,116,117,118,119,120,121,122,123,143,172,216,217,250,272,285,],[136,153,155,156,159,160,161,162,163,164,165,166,197,225,254,255,271,280,288,]),'super_exp':([100,104,105,106,116,117,118,119,120,121,122,123,143,172,216,217,250,272,285,],[137,137,137,137,137,137,137,137,137,137,137,137,137,137,137,137,137,137,137,]),'exp':([100,104,105,106,116,117,118,119,120,121,122,123,143,172,177,186,216,217,250,272,285,],[138,138,138,138,138,138,138,138,138,138,138,138,138,138,228,235,138,138,138,138,138,]),'termino':([100,104,105,106,116,117,118,119,120,121,122,123,143,172,177,186,191,216,217,250,272,285,],[139,139,139,139,139,139,139,139,139,139,139,139,139,139,139,139,238,139,139,139,139,139,]),'factor':([100,104,105,106,116,117,118,119,120,121,122,123,143,172,177,186,191,216,217,250,272,285,],[140,140,140,140,140,140,140,140,140,140,140,140,140,140,140,140,140,140,140,140,140,140,]),'varcte':([100,104,105,106,116,117,118,119,120,121,122,123,143,172,177,186,191,216,217,250,272,285,],[141,141,141,141,141,141,141,141,141,141,141,141,141,141,141,141,141,141,141,141,141,141,]),'mandar_parametros':([101,203,],[148,243,]),'escrituraD':([104,],[152,]),'hiper_expU':([137,],[171,]),'operadorL':([137,],[172,]),'super_expU':([138,],[176,]),'operadorR':([138,],[177,]),'expU':([139,],[185,]),'operadorA':([139,],[186,]),'terminoU':([140,],[190,]),'operadorT':([140,],[191,]),'mandar_parametrosD':([147,],[201,]),'recibir_parametrosD':([167,],[221,]),'neu_llamada':([204,],[244,]),'funcionesD':([224,],[261,]),'decisionU':([269,],[275,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAMA ID neu_programa PUNTOYCOMA variables funciones PRINCIPAL L_PAR R_PAR bloque empty','program',11,'p_programa','lexer_parser.py',234),
  ('variables -> VARIABLES variablesU','variables',2,'p_variales','lexer_parser.py',240),
  ('variables -> empty','variables',1,'p_variales','lexer_parser.py',241),
  ('variablesU -> variablesD','variablesU',1,'p_variales','lexer_parser.py',243),
  ('variablesU -> empty','variablesU',1,'p_variales','lexer_parser.py',244),
  ('variablesD -> ID neu_addVariableAStack COMA variablesD','variablesD',4,'p_variales','lexer_parser.py',246),
  ('variablesD -> ID DOSPUNTOS tipo_var neu_addVariable PUNTOYCOMA variablesU','variablesD',6,'p_variales','lexer_parser.py',247),
  ('funciones -> funcionesU','funciones',1,'p_funciones','lexer_parser.py',253),
  ('funciones -> empty','funciones',1,'p_funciones','lexer_parser.py',254),
  ('funcionesU -> tipo_funcion FUNCION ID neu_addFuncion L_PAR recibir_parametros R_PAR variables bloque funcionesD','funcionesU',10,'p_funciones','lexer_parser.py',256),
  ('funcionesD -> funciones','funcionesD',1,'p_funciones','lexer_parser.py',258),
  ('funcionesD -> empty','funcionesD',1,'p_funciones','lexer_parser.py',259),
  ('tipo_funcion -> ENTERO empty','tipo_funcion',2,'p_tipo_funcion','lexer_parser.py',265),
  ('tipo_funcion -> FLOTANTE empty','tipo_funcion',2,'p_tipo_funcion','lexer_parser.py',266),
  ('tipo_funcion -> CARACTER empty','tipo_funcion',2,'p_tipo_funcion','lexer_parser.py',267),
  ('tipo_funcion -> VOID empty','tipo_funcion',2,'p_tipo_funcion','lexer_parser.py',268),
  ('tipo_var -> ENTERO empty','tipo_var',2,'p_tipo_var','lexer_parser.py',274),
  ('tipo_var -> FLOTANTE empty','tipo_var',2,'p_tipo_var','lexer_parser.py',275),
  ('tipo_var -> CARACTER empty','tipo_var',2,'p_tipo_var','lexer_parser.py',276),
  ('recibir_parametros -> ID DOSPUNTOS tipo_var recibir_parametrosD empty','recibir_parametros',5,'p_recibir_parametros','lexer_parser.py',282),
  ('recibir_parametros -> empty','recibir_parametros',1,'p_recibir_parametros','lexer_parser.py',283),
  ('recibir_parametrosD -> COMA recibir_parametros empty','recibir_parametrosD',3,'p_recibir_parametros','lexer_parser.py',285),
  ('recibir_parametrosD -> empty','recibir_parametrosD',1,'p_recibir_parametros','lexer_parser.py',286),
  ('mandar_parametros -> ID mandar_parametrosD empty','mandar_parametros',3,'p_mandar_parametros','lexer_parser.py',291),
  ('mandar_parametros -> empty','mandar_parametros',1,'p_mandar_parametros','lexer_parser.py',292),
  ('mandar_parametrosD -> COMA mandar_parametros empty','mandar_parametrosD',3,'p_mandar_parametros','lexer_parser.py',294),
  ('mandar_parametrosD -> empty','mandar_parametrosD',1,'p_mandar_parametros','lexer_parser.py',295),
  ('bloque -> L_LLAVE bloqueU R_LLAVE empty','bloque',4,'p_bloque','lexer_parser.py',302),
  ('bloqueU -> estatuto bloqueD empty','bloqueU',3,'p_bloque','lexer_parser.py',304),
  ('bloqueU -> empty','bloqueU',1,'p_bloque','lexer_parser.py',305),
  ('bloqueD -> bloqueU empty','bloqueD',2,'p_bloque','lexer_parser.py',307),
  ('bloqueD -> empty','bloqueD',1,'p_bloque','lexer_parser.py',308),
  ('estatuto -> asignacion PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',313),
  ('estatuto -> llamada PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',314),
  ('estatuto -> retorno PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',315),
  ('estatuto -> lectura PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',316),
  ('estatuto -> escritura PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',317),
  ('estatuto -> decision empty','estatuto',2,'p_estatuto','lexer_parser.py',318),
  ('estatuto -> condicional empty','estatuto',2,'p_estatuto','lexer_parser.py',319),
  ('estatuto -> no_condicional empty','estatuto',2,'p_estatuto','lexer_parser.py',320),
  ('estatuto -> funciones_especiales PUNTOYCOMA empty','estatuto',3,'p_estatuto','lexer_parser.py',321),
  ('estatuto -> empty','estatuto',1,'p_estatuto','lexer_parser.py',322),
  ('asignacion -> ID IGUAL hiper_exp empty','asignacion',4,'p_asignacion','lexer_parser.py',327),
  ('llamada -> ID L_PAR mandar_parametros R_PAR neu_llamada empty','llamada',6,'p_llamada','lexer_parser.py',332),
  ('retorno -> REGRESA L_PAR ID R_PAR empty','retorno',5,'p_retorno','lexer_parser.py',338),
  ('lectura -> LEER L_PAR ID R_PAR empty','lectura',5,'p_lectura','lexer_parser.py',343),
  ('escritura -> ESCRIBIR L_PAR escrituraD R_PAR empty','escritura',5,'p_escritura','lexer_parser.py',348),
  ('escrituraD -> hiper_exp empty','escrituraD',2,'p_escritura','lexer_parser.py',350),
  ('escrituraD -> LETRERO empty','escrituraD',2,'p_escritura','lexer_parser.py',351),
  ('decision -> SI L_PAR hiper_exp R_PAR ENTONCES bloque decisionU empty','decision',8,'p_decision','lexer_parser.py',356),
  ('decisionU -> SINO bloque empty','decisionU',3,'p_decision','lexer_parser.py',358),
  ('decisionU -> empty','decisionU',1,'p_decision','lexer_parser.py',359),
  ('condicional -> MIENTRAS L_PAR hiper_exp R_PAR HACER bloque empty','condicional',7,'p_condicional','lexer_parser.py',364),
  ('no_condicional -> DESDE L_PAR asignacion R_PAR HASTA hiper_exp HACER bloque empty','no_condicional',9,'p_no_condicional','lexer_parser.py',369),
  ('funciones_especiales -> circulo empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',376),
  ('funciones_especiales -> color empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',377),
  ('funciones_especiales -> grosor empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',378),
  ('funciones_especiales -> linea empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',379),
  ('funciones_especiales -> puntoxy empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',380),
  ('funciones_especiales -> arco empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',381),
  ('funciones_especiales -> penup empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',382),
  ('funciones_especiales -> pendown empty','funciones_especiales',2,'p_funciones_especiales','lexer_parser.py',383),
  ('funciones_especiales -> empty','funciones_especiales',1,'p_funciones_especiales','lexer_parser.py',384),
  ('circulo -> CIRCULO L_PAR hiper_exp R_PAR empty','circulo',5,'p_circulo','lexer_parser.py',389),
  ('color -> COLOR L_PAR hiper_exp R_PAR empty','color',5,'p_color','lexer_parser.py',394),
  ('grosor -> GROSOR L_PAR hiper_exp R_PAR empty','grosor',5,'p_grosor','lexer_parser.py',399),
  ('linea -> LINEA L_PAR hiper_exp COMA hiper_exp COMA hiper_exp COMA hiper_exp R_PAR empty','linea',11,'p_linea','lexer_parser.py',404),
  ('puntoxy -> PUNTOXY L_PAR hiper_exp COMA hiper_exp R_PAR empty','puntoxy',7,'p_puntoxy','lexer_parser.py',409),
  ('arco -> ARCO L_PAR hiper_exp R_PAR empty','arco',5,'p_arco','lexer_parser.py',414),
  ('penup -> PENUP L_PAR hiper_exp R_PAR empty','penup',5,'p_penup','lexer_parser.py',419),
  ('pendown -> PENDOWN L_PAR hiper_exp R_PAR empty','pendown',5,'p_pendown','lexer_parser.py',424),
  ('operadorA -> MAS empty','operadorA',2,'p_operadorA','lexer_parser.py',431),
  ('operadorA -> MENOS empty','operadorA',2,'p_operadorA','lexer_parser.py',432),
  ('operadorT -> MULT empty','operadorT',2,'p_operadorT','lexer_parser.py',437),
  ('operadorT -> DIV empty','operadorT',2,'p_operadorT','lexer_parser.py',438),
  ('operadorL -> OR empty','operadorL',2,'p_operadorL','lexer_parser.py',443),
  ('operadorL -> AND empty','operadorL',2,'p_operadorL','lexer_parser.py',444),
  ('operadorR -> MENORQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',449),
  ('operadorR -> MAYORQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',450),
  ('operadorR -> MENORIGUALQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',451),
  ('operadorR -> MAYORIGUALQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',452),
  ('operadorR -> IGUALQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',453),
  ('operadorR -> DIFQUE empty','operadorR',2,'p_operadorR','lexer_parser.py',454),
  ('hiper_exp -> super_exp hiper_expU','hiper_exp',2,'p_hiper_exp','lexer_parser.py',461),
  ('hiper_expU -> operadorL hiper_exp empty','hiper_expU',3,'p_hiper_exp','lexer_parser.py',463),
  ('hiper_expU -> empty','hiper_expU',1,'p_hiper_exp','lexer_parser.py',464),
  ('super_exp -> exp super_expU','super_exp',2,'p_super_exp','lexer_parser.py',469),
  ('super_expU -> operadorR exp empty','super_expU',3,'p_super_exp','lexer_parser.py',471),
  ('super_expU -> empty','super_expU',1,'p_super_exp','lexer_parser.py',472),
  ('exp -> termino expU','exp',2,'p_exp','lexer_parser.py',477),
  ('expU -> operadorA exp','expU',2,'p_exp','lexer_parser.py',479),
  ('expU -> empty','expU',1,'p_exp','lexer_parser.py',480),
  ('termino -> factor terminoU','termino',2,'p_termino','lexer_parser.py',485),
  ('terminoU -> operadorT termino','terminoU',2,'p_termino','lexer_parser.py',487),
  ('terminoU -> empty','terminoU',1,'p_termino','lexer_parser.py',488),
  ('factor -> varcte empty','factor',2,'p_factor','lexer_parser.py',493),
  ('factor -> llamada empty','factor',2,'p_factor','lexer_parser.py',494),
  ('factor -> L_PAR hiper_exp R_PAR empty','factor',4,'p_factor','lexer_parser.py',495),
  ('varcte -> ID empty','varcte',2,'p_varcte','lexer_parser.py',502),
  ('varcte -> ENTEROVAL empty','varcte',2,'p_varcte','lexer_parser.py',503),
  ('varcte -> FLOTANTEVAL empty','varcte',2,'p_varcte','lexer_parser.py',504),
  ('varcte -> CARACTERVAL empty','varcte',2,'p_varcte','lexer_parser.py',505),
  ('empty -> <empty>','empty',0,'p_empty','lexer_parser.py',513),
  ('neu_programa -> <empty>','neu_programa',0,'p_neu_programa','lexer_parser.py',520),
  ('neu_addFuncion -> <empty>','neu_addFuncion',0,'p_neu_addFuncion','lexer_parser.py',530),
  ('neu_addVariable -> <empty>','neu_addVariable',0,'p_neu_addVariable','lexer_parser.py',539),
  ('neu_addVariableAStack -> <empty>','neu_addVariableAStack',0,'p_neu_addVariableAStack','lexer_parser.py',550),
  ('neu_llamada -> <empty>','neu_llamada',0,'p_neu_llamada','lexer_parser.py',559),
]
