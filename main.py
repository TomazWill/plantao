import json
from plantonista import Plantonista
from distribuicao import Distribuicao
from utils.read_json_file import ReadFileJson

# ------------------------------------------------------------
from datetime import datetime, date, time, timedelta, timezone
from calendar import monthrange

# Pegando dia e mês atual 
year = datetime.now().date().year
month = datetime.now().date().month

# Retorna dois valores inteiros (dia_semana, qtd_dias)
# O primeiro valor retorna dia da semana de 0(segunda-feira) a 6(domingo) por padrão
# O segundo valor retorna a quantidade de dias do mês 
qtd_dias_mes = monthrange(year, month)

# print(f"Quantidade de dias ({month}/{year}) => {qtd_dias_mes[1]}")
# ------------------------------------------------------------




# TODO: Fazer o uso da classe Plantonista
# plantonista = Plantonista(nome="", telefone="")

# Pegando informações que serão utilizadas para fazer a distribuição dos plantonistas no mês
jsonFile = ReadFileJson(file="dados/dados_post.json")
dados = jsonFile.getData()

distribuicao = Distribuicao()

# Fazendo a separação do mês (utilizando o mês atual) e fazendo a distribuição dos plantonistas
for dado in dados:
  if dado['mes'] == month:

    # O 'tipo-distribuicao' tem influência na distribuição dos dias dos plantonistas
    # Ela é responsável por dar mais flexibilidade na hora de passar as informações (que está no dados_post.json)
    # Quando é 'generico' significa que tem um padrão e que é repetido conforme a quantidade informada nas colunas 'revezamento-por-dias' e 'quem-inicia-o-mes' (do dados_post.json)
    # Quando é 'detalhado' precisa ser informado os dias que cada plantonista vai atuar 
    if dado['tipo-distribuicao'] == 'generico': 
      distribuicao.getDistribuicaoGenerica(dado, qtd_dias_mes[1])

    elif dado['tipo-distribuicao'] == 'detalhado':    
      distribuicao.getDistribuicaoDetalhada()
