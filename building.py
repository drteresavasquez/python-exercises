import datetime

class Building:
  
  def __init__(self, address, stories):
    # Establish the properties of each book
    # with a default value
    self.designer = "Dr. T"
    self.date_constructed = ""
    self.owner = ""
    self.address = address
    self.stories = stories

  def construct(self):
    self.date_constructed = datetime.datetime.now()
    
  def purchase(self, name):
    self.owner = name

# Create 5 building instances
# Have each one get purchased by a real estate magnate
# After purchased, construct each one
# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.

# building1 = Building("800 8th Street", 12)
# building1.purchase("Someone")
# building1.construct()
# print(f'{building1.address} was purchased by {building1.owner} on {building1.date_constructed} and has {building1.stories} stories')
