class CuboSemantico:

  # Hace retorno del tipo resultante de la operación entre 2 tipos
  def getTipoCubo(tipo1, tipo2, operador):
  
    # ENTERO
    if tipo1 == "ENTERO":
      if tipo2 == "ENTERO":
        return "ENTERO"
      elif tipo2 == "FLOTANTE":
        if operador == "+" or operador == "-" or operador == "*" or operador == "/":
          return "FLOTANTE"
        else:
          return "ENTERO"
      elif tipo2 == "CARACTER":
        return "ERROR"

    # FLOTANTE
    if tipo1 == "FLOTANTE":
      if tipo2 == "ENTERO" or tipo2 == "FLOTANTE":
        if operador == "+" or operador == "-" or operador == "*" or operador == "/":
          return "FLOTANTE"
        else:
          return "ENTERO"
      elif tipo2 == "CARACTER":
        return "ERROR"

    # CARACTER
    if tipo1 == "CARACTER":
      if tipo2 == "ENTERO" or tipo2 == "FLOTANTE":
        return "ERROR"
      elif tipo2 == "CARACTER":
        if operador == "+" or operador == "-" or operador == "*" or operador == "/":
          return "ERROR"
        else:
          return "ENTERO"

    return "ERROR"

# Pruebas
# print(CuboSemantico.getTipoCubo("ENTERO", "FLOTANTE", "+"))
# print(CuboSemantico.getTipoCubo("FLOTANTE", "ENTERO", "<"))
# print(CuboSemantico.getTipoCubo("CARACTER", "CARACTER", "!="))