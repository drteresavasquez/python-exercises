class City:
  
  def __init__(self, city, mayor, est):
    self.city = city
    self.mayor = mayor
    self.est = est
    self.buildings = list()
    
  def add_building(self, building):
    self.buildings.append(building)
    
  
    