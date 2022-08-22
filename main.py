import json
from utils.read_json_file import ReadFileJson

from on_duty_worker import OnDutyWorker
from distribution   import Distribution
from journey        import Journey

# Iniciando Jornada
journey = Journey()
print(journey)
print("---------------------------------")

# Pegando informações que serão utilizadas para fazer a distribuição dos plantonistas no mês
jsonFile = ReadFileJson(file="dados/dados_post.json")
list_of_months = jsonFile.get_full_data()

distribution = Distribution()

distribution.get_workers_of_current_month()
# print(f"Distribution:::\n {distribution.get_on_call_workers()}")


distribution.get_distribution_data_current_month(list_of_months, journey.month, journey.get_number_of_days_of_the_journey())
print(f"Distribution:::\n {distribution.get_on_call_workers()}")




# TODO: Fazer o uso da classe OnDutyWorker
# for i in range(0,10):
#   worker = OnDutyWorker(nome=f"Teste-{i}", telefone=f"{i}-123456789")
#   worker.add_worker_to_list()
#   print(f"[{i}] {worker.get_name()}")