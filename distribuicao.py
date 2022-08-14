

class Distribuicao():

  def getDistribuicaoGenerica(self, obj_mes, qtd_dias_mes):
    dia                           = 0
    revezamento_contador          = 0
    plantonista_contador          = 0
    qtd_de_plantonista            = len(obj_mes['plantonistas'])
    qtd_dias_plantonista_inicia   = obj_mes['quem-inicia-o-mes']['qtd-dias']
    revezamento_dias              = obj_mes['revezamento-por-dias']
    
    print(f"Quantidade de Plantonista: {qtd_de_plantonista}")

    while dia < qtd_dias_mes:
      
      if dia < qtd_dias_plantonista_inicia:
        self.imprimePlantonistaDoDia(dia, plantonista_inicia=True, mes=obj_mes, plantonista_contador=plantonista_contador)
        dia += 1
      else:

        # TODO: Precisa fazer verificação se o plantonista já deu inicio deve pular um dia no loop
        # if nome_plantonista_inicia == obj_mes['plantonistas'][plantonista_contador]['nome']:
        # print(f"DD: {dia+1} | Plant: {obj_mes['plantonistas'][plantonista_contador]['nome']}")
        
        # Quando a lista de plantonista chega ao fim precisa voltar ao inicio
        if  plantonista_contador == qtd_de_plantonista:
          plantonista_contador = self.mudaPlantonista(plantonista_contador, qtd_de_plantonista)

        # Imprime Plantonista conforme a quantidade de dias do revezamento (ex: revezamento_dias = 3)
        if revezamento_contador < revezamento_dias:
          revezamento_contador += 1
          self.imprimePlantonistaDoDia(dia=dia, plantonista_inicia=False, mes=obj_mes, plantonista_contador=plantonista_contador)
          dia += 1
        else:
          revezamento_contador = 0
          plantonista_contador = self.mudaPlantonista(plantonista_contador, qtd_de_plantonista)



  def imprimePlantonistaDoDia(self, dia, plantonista_inicia, mes, plantonista_contador):
    if plantonista_inicia == True:
      print(f"Dia: {dia+1} | Plantonista: {mes['quem-inicia-o-mes']['nome']}")
    else:
      print(f"Dia: {dia+1} | Plantonista: {mes['plantonistas'][plantonista_contador]['nome']}")
      

  def mudaPlantonista(self, plantonista_contador, qtd_de_plantonista):
    if plantonista_contador == qtd_de_plantonista:
      plantonista_contador = 0
    else:
      plantonista_contador += 1
    return plantonista_contador


  def getDistribuicaoDetalhada(self):
    print('Aqui Detalhado')