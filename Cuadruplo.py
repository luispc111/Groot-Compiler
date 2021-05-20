class Cuadruplo:

  # Constructor
  def __init__(self, operador, operando_i, operando_d, temporal):
    self.operador = operador
    self.operando_i = operando_i
    self.operando_d = operando_d
    self.temporal = temporal

  # Retorna un cuadruplo
  def getCuadruplo(self):
      return [self.operador, self.operando_i, self.operando_d, self.temporal]
