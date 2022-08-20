from datetime import datetime, date, time, timedelta, timezone
from calendar import monthrange


class Date():
  '''
  'Date' é uma classe reservada para trabalhar com datas.
  No momento ela é muito util para retornar o mês ou ano atual
  '''
  
  def get_month(self):
    return datetime.now().date().month

  def get_year(self):
    return datetime.now().date().year

  def get_number_of_days_in_the_current_month(self, month, year):
    '''
    ************ Função 'monthrange()' ************
    RETORNO: 2 valores inteiros:
    [0] Dia da semana de 0(segunda-feira) à 6(domingo) por padrão
    [1] A quantidade de dias do mês
    '''
    return monthrange(year, month)
