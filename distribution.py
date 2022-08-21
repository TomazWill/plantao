

class Distribution():
  # def __init__(self):
  #   self.plantonistas = plantonistas

  def get_generic_distribution(self, obj_mes, qtd_dias_mes):
    dia                           = 0
    revezamento_contador          = 0
    plantonista_contador          = 0
    qtd_de_plantonista            = len(obj_mes['plantonistas'])
    qtd_dias_plantonista_inicial  = obj_mes['quem-inicia-o-mes']['qtd-dias']
    nome_plantonista_inicial      = obj_mes['quem-inicia-o-mes']['nome']
    revezamento_dias              = obj_mes['revezamento-por-dias']
    fez_correcao_revezamento      = False

    while dia < qtd_dias_mes:
      # Verificação no segundo dia (variavel 'dia' inicia com 0) 
      # Se o plantonista já deu inicio deve atualizar o contador na mesma quantidade que ele deu inicio
      if not fez_correcao_revezamento:
        fez_correcao_revezamento = True
        revezamento_contador = self.change_workers_counter(
          nome_plantonista_inicial, 
          qtd_dias_plantonista_inicial, 
          obj_mes['plantonistas'], 
          plantonista_contador,
          revezamento_contador
        )

      # Verifica se 'qtd_dias_plantonista_inicial' é maior que 'revezamento_dias'
      # se for verdade ele para a aplicação, pois não confere com a regra da aplicação.
      if self.validate_number_of_days(qtd_dias_plantonista_inicial, revezamento_dias):
        break

      # Quando a lista de plantonista chega ao fim precisa voltar ao inicio
      if plantonista_contador == qtd_de_plantonista:
        plantonista_contador = self.change_worker(plantonista_contador, qtd_de_plantonista)

      # Imprime Plantonista conforme a quantidade de dias do revezamento (ex: revezamento_dias = 3)
      if revezamento_contador < revezamento_dias:
        revezamento_contador += 1
        self.get_worker_on_call_per_day(dia, False, obj_mes, plantonista_contador)
        dia += 1
      else:
        revezamento_contador = 0
        plantonista_contador = self.change_worker(plantonista_contador, qtd_de_plantonista)



  def validate_number_of_days(self, qtd_dias_plantonista_inicial, revezamento_dias):
    if qtd_dias_plantonista_inicial > revezamento_dias:
      print("-------------------------------[ERROR]--------------------------------")
      print(f"O valor de 'qtd_dias_plantonista_inicial'({qtd_dias_plantonista_inicial})")
      print(f"Não pode passar da quantidade do 'revezamento_dias'({revezamento_dias})")
      print("----------------------------------------------------------------------")
      return True
    else:
      return False


  # Método que atualiza o 'revezamento_contador' (retornando a correção para que não repita o plantonista)
  def change_workers_counter(self, nome_plantonista_inicial, qtd_dias_plantonista_inicial, obj_plantonistas, plantonista_contador, revezamento_contador):
    revezamento = 0

    # TODO: FAZER UMA BUSCA PARA SABER QUAL É O INDEX DO "nome_plantonista_inicial" NA LISTA DOS PLANTONISTAS
    #       COM ISSO PRECISARIA REORDENAR A LISTA COLOCANDO O quem-inicia-o-mes COMO PRIMEIRO, COM ISSO RESOLVERIA

    # Pernalonga == Gaguinho
    if nome_plantonista_inicial == obj_plantonistas[plantonista_contador]['nome']:
      if qtd_dias_plantonista_inicial == 3:
        revezamento = revezamento_contador + 0
      elif qtd_dias_plantonista_inicial == 2:
        revezamento = revezamento_contador + 1
      elif qtd_dias_plantonista_inicial == 1:
        revezamento = revezamento_contador + 2
      
    return revezamento


  def get_worker_on_call_per_day(self, dia, plantonista_inicia, mes, plantonista_contador):
    if plantonista_inicia == True:
      print(f"Dia: {dia+1} | Plantonista: {mes['quem-inicia-o-mes']['nome']}")
    else:
      print(f"Dia: {dia+1} | Plantonista: {mes['plantonistas'][plantonista_contador]['nome']}")
      

  def change_worker(self, plantonista_contador, qtd_de_plantonista):
    if plantonista_contador == qtd_de_plantonista:
      plantonista_contador = 0
    else:
      plantonista_contador += 1
    return plantonista_contador


  def get_detailed_distribution(self):
    print('Aqui Detalhado')