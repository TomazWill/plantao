from distribution import Distribution

class DetailedDistribution(Distribution):
  def __init__(self):
    super().__init__()

  def get_generic_distribution(self, month_object, number_of_days_in_the_month):
    day                               = 0
    on_call_workers__counter          = 0
    on_call_workers__number           = len(month_object['plantonistas'])
    rotation__counter                 = 0
    rotation__by_days                 = month_object['revezamento-por-dias']
    rotation__correction_was_made     = False
    who_starts_the_month__name        = month_object['quem-inicia-o-mes']['nome']
    who_starts_the_month__number_days = month_object['quem-inicia-o-mes']['qtd-dias']

    while day < number_of_days_in_the_month:
      # Verificação no segundo dia (variavel 'day' inicia com 0) 
      # Se o plantonista já deu inicio deve atualizar o contador na mesma quantidade que ele deu inicio
      if not rotation__correction_was_made:
        rotation__correction_was_made = True
        rotation__counter = self.change_rotation__counter(
          who_starts_the_month__name, 
          who_starts_the_month__number_days, 
          month_object['plantonistas'], 
          on_call_workers__counter,
          rotation__counter
        )

      # Verifica se 'who_starts_the_month__number_days' é maior que 'rotation__by_days'
      # se for verdade ele para a aplicação, pois não confere com a regra da aplicação.
      if self.validate_number_of_days(who_starts_the_month__number_days, rotation__by_days):
        break

      # Quando a lista de plantonista chega ao fim precisa voltar ao inicio
      if on_call_workers__counter == on_call_workers__number:
        on_call_workers__counter = self.change_worker(on_call_workers__counter, on_call_workers__number)

      # Imprime Plantonista conforme a quantidade de dias do revezamento (ex: rotation__by_days = 3)
      if rotation__counter < rotation__by_days:
        rotation__counter += 1
        self.save_worker_on_call_per_day(day, month_object, on_call_workers__counter)
        day += 1
      else:
        rotation__counter = 0
        on_call_workers__counter = self.change_worker(on_call_workers__counter, on_call_workers__number)