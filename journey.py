from utils.date import Date

class Journey(Date):
  '''
  Jornada contém a quantidade de dias no mês atual, 
  para dar sequencia na distribuição dos Plantonistas.
  '''

  def __init__(self):
    self.month = 0
    self.year = 0
    self.number_of_days_in_the_current_month = 0
    self.get_start_journey()

  def get_start_journey(self):
    self.month = self.get_month()
    self.year = self.get_year()
    self.number_of_days_in_the_current_month = self.get_number_of_days_in_the_current_month(self.month, self.year)

  def get_number_of_days_of_the_journey(self):
    return self.number_of_days_in_the_current_month[1]

  def __str__(self):
    return (f"[{self.month}/{self.year}] Dias da Jornada: {self.number_of_days_in_the_current_month[1]}")
