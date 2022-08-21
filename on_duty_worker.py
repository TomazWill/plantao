from worker import Worker

class OnDutyWorker(Worker):
  def __init__(self, nome, telefone):
    super().__init__(nome, telefone)
    self._list_of_on_call_workers = []

  def add_worker_to_list(self):
    self._list_of_on_call_workers.append(self.get_name)

  def get_list_of_on_call_workers(self):
    return self._list_of_on_call_workers

  def __str__(self):
    return f"Nome: {self._nome} | Telefone {self._telefone}"