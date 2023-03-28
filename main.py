from building import Building
from city import City

megalopolis = City("megalopolis", "mayor", 1999)

building1 = Building("800 8th Street", 12)
building1.purchase("Jessup")
building1.construct()

megalopolis.add_building(building1)

for building in megalopolis.buildings:
  print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories')



