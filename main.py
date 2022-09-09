import json
from utils.read_json_file   import ReadFileJson

from on_duty_worker         import OnDutyWorker
from generic_distribution   import GenericDistribution
from journey                import Journey

# Iniciando Jornada
journey = Journey()
print(journey)
print("---------------------------------")

# Pegando informações que serão utilizadas para fazer a distribuição dos plantonistas no mês
jsonFile = ReadFileJson(file="dados/dados_post.json")
list_of_months = jsonFile.get_full_data()

genericDistribution = GenericDistribution()
current_month_object = genericDistribution.filter_data_current_month(list_of_months, journey.month)


# Faz separação dos plantonistas em uma lista para ser ordenada e utilizada na distribuição
genericDistribution.set_workers_of_current_month(current_month_object)

# Inicia processo da distribuição das datas
genericDistribution.get_distribution_data_current_month(current_month_object, journey.get_number_of_days_of_the_journey())
genericDistribution.print_on_call_workers_by_current_month()


# TODO: Os tipos de distribuição serão classes separadas
# Vai ter uma classe principal(Distribution) e duas distintas:
# - Distribution
#   - GenericDistribution
#   - DetailedDistribution
