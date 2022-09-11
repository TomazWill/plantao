from constants import DETAILED_DISTRIBUTION_TYPE, GENERIC_DISTRIBUTION_TYPE
from on_duty_worker import OnDutyWorker

class Distribution(OnDutyWorker):
  def __init__(self):
    self.on_call_workers_by_day = []
    self.list_of_on_call_workers_name = []

  def set_on_call_workers_in_current_month(self, day_and_worker):
    self.on_call_workers_by_day.append(day_and_worker)

  def set_worker_name_to_list(self, name):
    self.list_of_on_call_workers_name.append(name)

  def set_in_first_position_list_of_on_duty_worker(self, worker, list_worker):
    '''Adiciona elemento na primeira posição na lista'''
    list_worker.insert(0, worker)

  def set_workers_of_current_month(self, month_object):
    '''Faz separação dos plantonistas em uma lista para ser ordenada e utilizada na distribuição'''
    for i in month_object['plantonistas']:
      on_duty_worker = OnDutyWorker(i['nome'], i['telefone'])
      self.set_worker_name_to_list(on_duty_worker.get_name())

  def get_on_call_workers_by_current_month(self):
    '''Retorna a lista distribuida dos trabalhadores (mês atual)'''
    return self.on_call_workers_by_day

  def print_on_call_workers_by_current_month(self):
    '''Mostra a lista distribuida dos trabalhadores (mês atual)'''
    for i in self.on_call_workers_by_day:
      print(f"Day: {i['day']} | Worker: {i['worker']}")

  def get_list_of_on_duty_worker(self):
    '''Retorna uma lista com os nomes dos trabalhadores (mês atual)'''
    return self.list_of_on_call_workers_name

  def delete_by_index(self, index, list_worker):
    list_worker.pop(index)

  def find_worker_by_name(self, worker_name, list_worker):
    '''Procura o trabalhador e retorna o indice'''
    return list_worker.index(worker_name)

  def filter_data_current_month(self, list_of_months, current_month):
    '''Retorna os dados o mês atual'''
    for month_object in list_of_months:
      if month_object['mes'] == current_month:
          return month_object

  def reorder_list_of_on_duty_worker(self, worker_name, list_worker):
    worker_index = self.find_worker_by_name(worker_name, list_worker)
    self.delete_by_index(worker_index, list_worker)
    self.set_in_first_position_list_of_on_duty_worker(worker_name, list_worker)
    return list_worker



  def isGenericDistribution(self, month_object):
    '''Quando é 'generico' significa que tem um padrão e que é repetido conforme a quantidade informada 
       nas colunas 'revezamento-por-dias' e 'quem-inicia-o-mes' (do dados_post.json);
       Quando é 'detalhado' precisa ser informado os dias que cada plantonista vai atuar;
    '''
    if month_object['tipo-distribuicao'] == GENERIC_DISTRIBUTION_TYPE:
      return True
    elif month_object['tipo-distribuicao'] == DETAILED_DISTRIBUTION_TYPE:
      return False


  def validate_number_of_days(self, who_starts_the_month__number_days, rotation__by_days):
    if who_starts_the_month__number_days > rotation__by_days:
      print("-------------------------------[ERROR]--------------------------------")
      print(f"O valor de 'who_starts_the_month__number_days'({who_starts_the_month__number_days})")
      print(f"Não pode passar da quantidade do 'rotation__by_days'({rotation__by_days})")
      print("----------------------------------------------------------------------")
      return True
    else:
      return False


  # Método que atualiza o 'rotation__counter' (retornando a correção para que não repita o plantonista)
  def change_rotation__counter(self, who_starts_the_month__name, 
                              who_starts_the_month__number_days, 
                              obj_plantonistas, on_call_workers__counter, 
                              rotation__counter):
    rotation = 0

    # Fazendo a reordenação da lista conforme 'quem-inicia-o-mes'
    list_of_on_duty_worker = self.reorder_list_of_on_duty_worker(who_starts_the_month__name, self.get_list_of_on_duty_worker())

    if who_starts_the_month__name == list_of_on_duty_worker[on_call_workers__counter]:
      if who_starts_the_month__number_days == 3:
        rotation = rotation__counter + 0
      elif who_starts_the_month__number_days == 2:
        rotation = rotation__counter + 1
      elif who_starts_the_month__number_days == 1:
        rotation = rotation__counter + 2
    return rotation

  def save_worker_on_call_per_day(self, day, on_call_workers__counter):
    list_of_on_duty_worker = self.get_list_of_on_duty_worker()
    self.set_on_call_workers_in_current_month({'day':day+1, 'worker':list_of_on_duty_worker[on_call_workers__counter]})

  def change_worker(self, on_call_workers__counter, on_call_workers__number):
    if on_call_workers__counter == on_call_workers__number:
      on_call_workers__counter = 0
    else:
      on_call_workers__counter += 1
    return on_call_workers__counter



