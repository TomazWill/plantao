from constants import DETAILED_DISTRIBUTION_TYPE
from distribution import Distribution

class DetailedDistribution(Distribution):
  def __init__(self):
    super().__init__()

  def get_distribution_data_current_month(self, month_object, number_of_days_of_the_journey):
    if month_object['tipo-distribuicao'] == DETAILED_DISTRIBUTION_TYPE:    
      self.get_detailed_distribution()

  def get_detailed_distribution(self):
    print('Aqui Detalhado')