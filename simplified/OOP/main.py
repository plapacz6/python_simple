class Guitar:
  def __init__(self, n_string = 6):
      self.n_string = n_string
      self.play()
      self.__realCost = 10
  def play(self):
    print("pam pam pam pam pam")

my_guitar = Guitar()
print(my_guitar.n_string)
my_guitar.play()


class OtherGuitar(Guitar):
  pass

my_guitarO = OtherGuitar()
print(my_guitarO.n_string)
my_guitarO.play()


class ElectricGuitar(Guitar):
  def __init__(self):
      super().__init__()
      self.n_string = 8
      self.color = ("#000000", "#FFFFFF")
      self.__officialCost = 50      

  def __printCost(self):
    print("its cost me ", self._Guitar__realCost, " only")
      
  def playLouder(self):
    print("pam pam pam pam pam".upper())

my_guitarE = ElectricGuitar()
print(my_guitarE.n_string)
my_guitarE.play()
my_guitarE.playLouder()
print(my_guitar.n_string)
#print("not private cost", my_guitarE.__officialCost)  #AtrributeError
print("not private cost", my_guitarE._ElectricGuitar__officialCost)
#my_guitarE.__printCost()
my_guitarE._ElectricGuitar__printCost()

class BassGuitar(Guitar):
  def __init__(self, n_string = 4):
      super().__init__(n_string)

my_guitarB = BassGuitar()
my_guitarB.play
print(my_guitarB.n_string)



