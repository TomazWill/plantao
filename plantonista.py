

class Plantonista():
  def __init__(self, nome, telefone):
    self._nome = nome
    self._telefone = telefone

  def __str__(self):
    return self._nome