from distribution import Distribution

class DetailedDistribution(Distribution):
  def __init__(self):
    super().__init__()

  def reorder_list_of_on_duty_worker(self):
    '''Faz a reordenação da 'lista dos plantonistas' pelos dias crescente (1,2..29,30)'''
    list_of_on_duty_worker = self.get_on_call_workers_by_current_month()
    sortedByDay = sorted(list_of_on_duty_worker, key=lambda x: x['day'])
    self.on_call_workers_by_day = sortedByDay

  def get_detailed_distribution(self, month_object, number_of_days_in_the_month):
    for worker in month_object['plantonistas']:
      index_worker = self.find_worker_by_name(worker['nome'], self.get_list_of_on_duty_worker())
      for day in worker['dias-do-plantao']:
        self.save_worker_on_call_per_day(day-1, index_worker)

    self.reorder_list_of_on_duty_worker()