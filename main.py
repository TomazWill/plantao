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
current_month_object = distribution.filter_data_current_month(list_of_months, journey.month)



distribution.set_workers_of_current_month(current_month_object)
print(distribution.get_list_of_on_duty_worker())


# for i in distribution.get_workers_of_current_month(current_month_object):
#   on_duty_worker = OnDutyWorker(nome=f"{i['nome']}", telefone=f"{i['telefone']}")
#   on_duty_worker.add_worker_to_list()
#   print(f"{on_duty_worker.get_name()}")
  # print(f"Nome: {i['nome']} | Telefone: {i['telefone']}")

# TODO: Precisa começar a trabalhar em uma função que faz a alteração da ordem dos plantonistas


distribution.get_distribution_data_current_month(current_month_object, journey.get_number_of_days_of_the_journey())
# print(distribution.get_on_call_workers())



