import json
from utils.read_json_file import ReadFileJson

from constants    import GENERIC_DISTRIBUTION_TYPE, DETAILED_DISTRIBUTION_TYPE
from plantonista  import Plantonista
from distribution import Distribution
from journey      import Journey

# Iniciando Jornada
journey = Journey()
print(journey)
print("---------------------------------")


# TODO: Fazer o uso da classe Plantonista
# plantonista = Plantonista(nome="", telefone="")



# Pegando informações que serão utilizadas para fazer a distribuição dos plantonistas no mês
jsonFile = ReadFileJson(file="dados/dados_post.json")
obj_todos_meses = jsonFile.get_full_data()

distribution = Distribution()

# Fazendo a separação do mês (utilizando o mês atual) e fazendo a distribuição dos plantonistas
for obj_mes in obj_todos_meses:
  if obj_mes['mes'] == journey.month:

    # O 'tipo-distribuicao' tem influência na distribuição dos dias dos plantonistas
    # Ela é responsável por dar mais flexibilidade na hora de passar as informações (que está no dados_post.json)
    # Quando é 'generico' significa que tem um padrão e que é repetido conforme a quantidade informada nas colunas 'revezamento-por-dias' e 'quem-inicia-o-mes' (do dados_post.json)
    # Quando é 'detalhado' precisa ser informado os dias que cada plantonista vai atuar 
    if obj_mes['tipo-distribuicao'] == GENERIC_DISTRIBUTION_TYPE: 
      distribution.get_generic_distribution(obj_mes, journey.get_number_of_days_of_the_journey())

    elif obj_mes['tipo-distribuicao'] == DETAILED_DISTRIBUTION_TYPE:    
      distribution.get_detailed_distribution()
