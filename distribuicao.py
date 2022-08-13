

class Distribuicao():

  def getDistribuicaoGenerica(self, obj, qtd_dias_mes):
    dia                           = 0
    revezamento_contador          = 0
    plantonista_contador          = 0
    qtd_de_plantonista            = len(obj['plantonistas'])
    qtd_dias_plantonista_inicia   = obj['quem-inicia-o-mes']['qtd-dias']
    nome_plantonista_inicia       = obj['quem-inicia-o-mes']['nome']
    revezamento_dias              = obj['revezamento-por-dias']
    
    print(f"Quantidade de Plantonista: {qtd_de_plantonista}")

    while dia < qtd_dias_mes:
      
      if dia < qtd_dias_plantonista_inicia:
        print(f"Dia: {dia+1} | Plantonista: {nome_plantonista_inicia}")
        dia += 1
      else:

        # TODO: Precisa fazer verificação se o plantonista já deu inicio deve pular um dia no loop
        # if nome_plantonista_inicia == obj['plantonistas'][plantonista_contador]['nome']:
        # print(f"DD: {dia+1} | Plant: {obj['plantonistas'][plantonista_contador]['nome']}")
        
        # Quando a lista de plantonista chega ao fim precisa voltar ao inicio
        if  plantonista_contador == qtd_de_plantonista:
          plantonista_contador = self.mudaPlantonista(plantonista_contador, qtd_de_plantonista)

        # Imprime Plantonista conforme a quantidade de dias do revezamento (ex: revezamento_dias = 3)
        if revezamento_contador < revezamento_dias:
          revezamento_contador += 1
          self.imprimePlantonistaDoDia(dia, obj, plantonista_contador, qtd_de_plantonista)
          dia += 1
        else:
          revezamento_contador = 0
          plantonista_contador = self.mudaPlantonista(plantonista_contador, qtd_de_plantonista)



  def imprimePlantonistaDoDia(self, dia, obj, plantonista_contador, qtd_de_plantonista):
    print(f"Dia: {dia+1} | Plantonista: {obj['plantonistas'][plantonista_contador]['nome']}")
      

  def mudaPlantonista(self, plantonista_contador, qtd_de_plantonista):
    if plantonista_contador == qtd_de_plantonista:
      plantonista_contador = 0
    else:
      plantonista_contador += 1
    return plantonista_contador


  def getDistribuicaoDetalhada(self):
    print('Aqui Detalhado')