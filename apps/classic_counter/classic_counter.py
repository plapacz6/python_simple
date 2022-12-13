# author: plapacz6@gmail.com,  date: 2022-12-14,  licence: GPLv3
#
# classic counter
#


class wheel():

  def __init__(self, stepVals_):
    self.stepNumber = len(stepVals_)
    if self.stepNumber < 2: ## counter must have at least 2 steps
      #raise ValueError 
      raise AssertionError
    self.stepVals = stepVals_
    self.currStep = 0
    self.currVal = self.stepVals[self.currStep]

  def __str__(self):
    return str(self.currVal)

  def __iter__(self):
    pass

  def __next__(self):
    pass


#wheelDef - list of step on each position of counter
class wheelCounter():

  def __init__(self, wheelsSymb):
    #print(wheelsSymb)
    self.cnLen = len(wheelsSymb)
    #print(self.cnLen)
    if self.cnLen < 1:  
      #raise ValueError 
      raise AssertionError
    self.cn = []
    for i in range(self.cnLen):
      #print(wheelsSymb[i])
      self.cn.append( wheel(wheelsSymb[i] if len(wheelsSymb[i]) > 0 else []))

  def __str__(self):
    cn_view = []
    for i in range(self.cnLen):
      cn_view.append(self.cn[i].__str__())
    return ':'.join(cn_view)
      



if __name__ == "__main__":
  print("test module 'classical counter'")
  counter = wheelCounter([
     [ ("{}".format(x)).zfill(2) for x in range(0, 24) ],\
     [ (str(x)).zfill(2) for x in  range(0, 60) ],\
     [ (str(x)).zfill(2) for x in  range(0, 10) ]\
     ])
  print(counter)
