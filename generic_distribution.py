from distribution import Distribution

class GenericDistribution(Distribution):

  def get_generic_distribution(self, month_object, number_of_days_in_the_month):
    '''A Distribuição Genérica segue um padrão que é repetido conforme 
       a quantidade informada nas colunas 'revezamento-por-dias' 
       e 'quem-inicia-o-mes' (do dados_post.json).'''
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
        self.save_worker_on_call_per_day(day, on_call_workers__counter)
        day += 1
      else:
        rotation__counter = 0
        on_call_workers__counter = self.change_worker(on_call_workers__counter, on_call_workers__number)


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
      if who_starts_the_month__number_days == 4:
        rotation = rotation__counter + 0
      elif who_starts_the_month__number_days == 3:
        rotation = rotation__counter + 1
      elif who_starts_the_month__number_days == 2:
        rotation = rotation__counter + 2
      elif who_starts_the_month__number_days == 1:
        rotation = rotation__counter + 3
    return rotation


  def change_worker(self, on_call_workers__counter, on_call_workers__number):
    if on_call_workers__counter == on_call_workers__number:
      on_call_workers__counter = 0
    else:
      on_call_workers__counter += 1
    return on_call_workers__counter
  