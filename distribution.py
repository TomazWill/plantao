from constants import GENERIC_DISTRIBUTION_TYPE, DETAILED_DISTRIBUTION_TYPE


class Distribution():
  def __init__(self):
    self.on_call_workers = []

  def set_on_call_workers(self, day_and_worker):
    self.on_call_workers.append(day_and_worker)

  def get_on_call_workers(self):
    return self.on_call_workers

  def get_workers_of_current_month(self):
    # for i in range(0,10):
    #   worker = OnDutyWorker(nome=f"Teste-{i}", telefone=f"{i}-123456789")
    #   worker.add_worker_to_list()
    #   print(f"[{i}] {worker.get_name()}")
    
    # TODO: Continuar aqui, precisa pegar os workers e adicionar na lista com método add_worker_to_list (OnDutyWorker).
    # month_object['plantonistas']
    
    pass

  def get_distribution_data_current_month(self, list_of_months, current_month, number_of_days_of_the_journey):
    '''Faz a separação do mês (utilizando o mês atual) e fazendo a distribuição dos plantonistas'''
    for month_object in list_of_months:
      if month_object['mes'] == current_month:
        # O 'tipo-distribuicao' tem influência na distribuição dos dias dos plantonistas
        # Ela é responsável por dar mais flexibilidade na hora de passar as informações (que está no dados_post.json)
        # Quando é 'generico' significa que tem um padrão e que é repetido conforme a quantidade informada nas colunas 'revezamento-por-dias' e 'quem-inicia-o-mes' (do dados_post.json)
        # Quando é 'detalhado' precisa ser informado os dias que cada plantonista vai atuar 
        if month_object['tipo-distribuicao'] == GENERIC_DISTRIBUTION_TYPE: 
          self.get_generic_distribution(month_object, number_of_days_of_the_journey)
        elif month_object['tipo-distribuicao'] == DETAILED_DISTRIBUTION_TYPE:    
          self.get_detailed_distribution()

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
        self.save_worker_on_call_per_day(day, False, month_object, on_call_workers__counter)
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

    # TODO: FAZER UMA BUSCA PARA SABER QUAL É O INDEX DO "who_starts_the_month__name" NA LISTA DOS PLANTONISTAS
    #       COM ISSO PRECISARIA REORDENAR A LISTA COLOCANDO O quem-inicia-o-mes COMO PRIMEIRO, COM ISSO RESOLVERIA

    # Pernalonga == Gaguinho
    if who_starts_the_month__name == obj_plantonistas[on_call_workers__counter]['nome']:
      if who_starts_the_month__number_days == 3:
        rotation = rotation__counter + 0
      elif who_starts_the_month__number_days == 2:
        rotation = rotation__counter + 1
      elif who_starts_the_month__number_days == 1:
        rotation = rotation__counter + 2
      
    return rotation


  def save_worker_on_call_per_day(self, day, is_the_first_worker, mes, on_call_workers__counter):
    if is_the_first_worker == True:
      self.set_on_call_workers({'day':day+1, 'month':mes['quem-inicia-o-mes']['nome']})
      # print(f"Dia: {day+1} | Plantonista: {mes['quem-inicia-o-mes']['nome']}")
    else:
      self.set_on_call_workers({'day':day+1, 'month':mes['plantonistas'][on_call_workers__counter]['nome']})
      # print(f"Dia: {day+1} | Plantonista: {mes['plantonistas'][on_call_workers__counter]['nome']}")
      

  def change_worker(self, on_call_workers__counter, on_call_workers__number):
    if on_call_workers__counter == on_call_workers__number:
      on_call_workers__counter = 0
    else:
      on_call_workers__counter += 1
    return on_call_workers__counter


  def get_detailed_distribution(self):
    print('Aqui Detalhado')