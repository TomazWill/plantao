from constants import DETAILED_DISTRIBUTION_TYPE, GENERIC_DISTRIBUTION_TYPE
from on_duty_worker import OnDutyWorker

class Distribution(OnDutyWorker):
  def __init__(self):
    self.on_call_workers_by_day = []
    self.list_of_on_call_workers_name = []

  # MÉTODOS CHAMADOS APENAS NESSA CLASSE PAI
  def set_on_call_workers_in_current_month(self, day_and_worker):
    self.on_call_workers_by_day.append(day_and_worker)

  def set_worker_name_to_list(self, name):
    self.list_of_on_call_workers_name.append(name)

  def set_in_first_position_list_of_on_duty_worker(self, worker, list_worker):
    '''Adiciona elemento na primeira posição na lista'''
    list_worker.insert(0, worker)

  def delete_by_index(self, index, list_worker):
    list_worker.pop(index)

  def get_worker_by_name(self, worker_name, list_worker):
    '''Procura o trabalhador e retorna o indice'''
    return list_worker.index(worker_name)

  # MÉTODOS UTILIZADOS PELOS FILHOS (HERANÇA)
  def get_list_of_on_duty_worker(self):
    '''Retorna uma lista com os nomes dos trabalhadores (mês atual)'''
    return self.list_of_on_call_workers_name

  def reorder_list_of_on_duty_worker(self, worker_name, list_worker):
    worker_index = self.get_worker_by_name(worker_name, list_worker)
    self.delete_by_index(worker_index, list_worker)
    self.set_in_first_position_list_of_on_duty_worker(worker_name, list_worker)
    return list_worker

  def save_worker_on_call_per_day(self, day, on_call_workers__counter):
    list_of_on_duty_worker = self.get_list_of_on_duty_worker()
    self.set_on_call_workers_in_current_month({'day':day+1, 'worker':list_of_on_duty_worker[on_call_workers__counter]})

  # MÉTODOS UTILIZADOS PELO MAIN (INICIALIZADOR)
  def set_workers_of_current_month(self, month_object):
    '''Faz separação dos plantonistas em uma lista para ser ordenada e utilizada na distribuição'''
    for i in month_object['plantonistas']:
      on_duty_worker = OnDutyWorker(i['nome'], i['telefone'])
      self.set_worker_name_to_list(on_duty_worker.get_name())

  def isGenericDistribution(self, month_object):
    '''Quando é 'generico' significa que tem um padrão e que é repetido conforme a quantidade informada 
       nas colunas 'revezamento-por-dias' e 'quem-inicia-o-mes' (do dados_post.json);
       Quando é 'detalhado' precisa ser informado os dias que cada plantonista vai atuar;
    '''
    if month_object['tipo-distribuicao'] == GENERIC_DISTRIBUTION_TYPE:
      return True
    elif month_object['tipo-distribuicao'] == DETAILED_DISTRIBUTION_TYPE:
      return False

  def print_on_call_workers_by_current_month(self):
    '''Mostra a lista distribuída dos trabalhadores (mês atual)'''
    for i in self.on_call_workers_by_day:
      print(f"Day: {i['day']} | Worker: {i['worker']}")

