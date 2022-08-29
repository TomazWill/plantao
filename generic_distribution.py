from distribution import Distribution

class GenericDistribution(Distribution):
  def __init__(self):
    super().__init__()

  def get_detailed_distribution(self):
    print('Aqui Detalhado')