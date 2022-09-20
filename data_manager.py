
class DataManager():
  # Classe responsável por gerenciar informações que vem do Json
  
  def get_current_month(self, list_of_months, current_month):
    '''Retorna os dados o mês atual'''
    for month_object in list_of_months:
      if month_object['mes'] == current_month:
          return month_object
          