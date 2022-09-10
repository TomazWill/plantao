import json
from utils.read_json_file   import ReadFileJson

from on_duty_worker         import OnDutyWorker
from generic_distribution   import GenericDistribution
from detailed_distribution  import DetailedDistribution
from distribution           import Distribution
from journey                import Journey

# Iniciando Jornada
journey = Journey()
print(journey)
print("---------------------------------")

# Pegando informações que serão utilizadas para fazer a distribuição dos plantonistas no mês
jsonFile = ReadFileJson(file="dados/dados_post.json")
list_of_months = jsonFile.get_full_data()

# DISTRIBUIÇÃO
distribution = Distribution()
current_month_object = distribution.filter_data_current_month(list_of_months, journey.month)

if (distribution.isGenericDistribution(current_month_object)):
  # DISTRIBUIÇÃO GENERICA
  genericDistribution = GenericDistribution()
  genericDistribution.set_workers_of_current_month(current_month_object)
  genericDistribution.get_generic_distribution(current_month_object, journey.get_number_of_days_of_the_journey())
  genericDistribution.print_on_call_workers_by_current_month()
else:
  # DISTRIBUIÇÃO DETALHADA
  detailedDistribution = DetailedDistribution()
  detailedDistribution.set_workers_of_current_month(current_month_object)
  detailedDistribution.get_detailed_distribution(current_month_object, journey.get_number_of_days_of_the_journey())
  detailedDistribution.print_on_call_workers_by_current_month()

