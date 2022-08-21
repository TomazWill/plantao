

class Worker():
  def __init__(self, nome, telefone):
    self._nome = nome
    self._telefone = telefone

  def get_name(self):
    return self._nome  

  def get_telefone(self):
    return self._telefone  

  def __str__(self):
    return f"Nome: {self._nome} | Telefone {self._telefone}"