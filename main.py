import json
from utils.read_json_file import ReadFileJson

from constants      import GENERIC_DISTRIBUTION_TYPE, DETAILED_DISTRIBUTION_TYPE
from on_duty_worker import OnDutyWorker
from distribution   import Distribution
from journey        import Journey

# Iniciando Jornada
journey = Journey()
print(journey)
print("---------------------------------")


# TODO: Fazer o uso da classe OnDutyWorker
# for i in range(0,10):
#   worker = OnDutyWorker(nome=f"Teste-{i}", telefone=f"{i}-123456789")
#   worker.add_worker_to_list()
#   print(f"[{i}] {worker.get_name()}")



# Pegando informações que serão utilizadas para fazer a distribuição dos plantonistas no mês
jsonFile = ReadFileJson(file="dados/dados_post.json")
list_of_months = jsonFile.get_full_data()

distribution = Distribution()

# Fazendo a separação do mês (utilizando o mês atual) e fazendo a distribuição dos plantonistas
for month_object in list_of_months:
  if month_object['mes'] == journey.month:

    # O 'tipo-distribuicao' tem influência na distribuição dos dias dos plantonistas
    # Ela é responsável por dar mais flexibilidade na hora de passar as informações (que está no dados_post.json)
    # Quando é 'generico' significa que tem um padrão e que é repetido conforme a quantidade informada nas colunas 'revezamento-por-dias' e 'quem-inicia-o-mes' (do dados_post.json)
    # Quando é 'detalhado' precisa ser informado os dias que cada plantonista vai atuar 
    if month_object['tipo-distribuicao'] == GENERIC_DISTRIBUTION_TYPE: 
      distribution.get_generic_distribution(month_object, journey.get_number_of_days_of_the_journey())

    elif month_object['tipo-distribuicao'] == DETAILED_DISTRIBUTION_TYPE:    
      distribution.get_detailed_distribution()
