class CuboSemantico:

  # Hace retorno del tipo resultante de la operación entre 2 tipos
  def getTipoCubo(tipo1, tipo2, operador):
  
    # ENTERO
    if tipo1 == "Entero":
      if tipo2 == "Entero":
        return "Entero"
      elif tipo2 == "Flotante":
        if operador == "+" or operador == "-" or operador == "*" or operador == "/":
          return "Flotante"
        else:
          return "Entero"
      elif tipo2 == "Caracter":
        return "Error"

    # FLOTANTE
    if tipo1 == "Flotante":
      if tipo2 == "Entero" or tipo2 == "Flotante":
        if operador == "+" or operador == "-" or operador == "*" or operador == "/":
          return "Flotante"
        else:
          return "Entero"
      elif tipo2 == "Caracter":
        return "Error"

    # CARACTER
    if tipo1 == "CARACTER":
      if tipo2 == "Entero" or tipo2 == "Flotante":
        return "Error"
      elif tipo2 == "Caracter":
        if operador == "==" or operador == "!=":
          return "Entero"
        else:
          return "Error"

    return "Error"

# Pruebas
# print(CuboSemantico.getTipoCubo("ENTERO", "FLOTANTE", "+"))
# print(CuboSemantico.getTipoCubo("FLOTANTE", "ENTERO", "<"))
# print(CuboSemantico.getTipoCubo("CARACTER", "CARACTER", "!="))