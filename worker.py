

class Worker():
  def __init__(self, name, phone_number):
    self._name = name
    self._phone_number = phone_number

  def get_name(self):
    return self._name  

  def get_phone_number(self):
    return self._phone_number  

  def set_name(self, name):
    self._name = name

  def set_phone_number(self, phone_number):
    self._phone_number = phone_number

  def __str__(self):
    return f"Nome: {self.get_name()} | Telefone {self.get_phone_number()}"