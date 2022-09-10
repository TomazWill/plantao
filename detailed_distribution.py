from distribution import Distribution

class DetailedDistribution(Distribution):
  def __init__(self):
    super().__init__()

  def get_detailed_distribution(self, month_object, number_of_days_in_the_month):
    print(f'month_object::: {month_object}')
    print(f'number_of_days_in_the_month::: {number_of_days_in_the_month}')

    

    for worker in month_object['plantonistas']:
      index_worker = self.find_worker_by_name(worker['nome'], self.get_list_of_on_duty_worker())
      
      for day in worker['dias-do-plantao']:
        self.save_worker_on_call_per_day(day-1, index_worker)



# TODO: FALTA FAZER ORDENAÇÃO DOS VALORES 
# ANTES DE IMPRIMIR OU NA HORA DE SALVAR
# VALORES DO OBJETO FINAL:
# 00: {...}
# 01: {...}
# 02: {...}
# 03: {...}
# 04: {...}
