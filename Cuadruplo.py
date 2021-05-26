class Cuadruplo:

  # Constructor
  def __init__(self, operador, operando_i, operando_d, res):
    self.operador = operador
    self.operando_i = operando_i
    self.operando_d = operando_d
    self.res = res

  # Retorna un cuadruplo
  def getCuadruplo(self):
    return [self.operador, self.operando_i, self.operando_d, self.res]
