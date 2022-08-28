from worker import Worker

class OnDutyWorker(Worker):
  def __init__(self, name, phone_number):
    super().__init__(name, phone_number)

  def __str__(self):
    return f"Nome: {self.get_name()} | Telefone {self.get_phone_number()}"