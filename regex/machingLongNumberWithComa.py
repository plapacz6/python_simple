#
# date: 2021-08-20, autor: plapacz6@gmail.com

import re
testSet = [
  ['12', 1],
  ['446', 1],
  ['1,454',  1],
  ['34,989', 1],
  ['994,431', 1],
  ['4,233,210',1],
  ['99,234,219', 1],
  ['434,200,871', 1],
  ['4,991,090,234', 1],
  ['452434', 0],
  ['56,8824', 0],
  ['98,44,799', 0]
]

def isNumberWithComa(n):
  #TODO: incorrect regexpression  
  reNumWithComa = r'(\d{0,3},)*(\d{3},)*(\d{0,3}?)'
  objReNWC = re.compile(reNumWithComa)
  mo = objReNWC.search(n)
  if len(mo.group()) > 0:
    return True
  return False

numberOfTest = 0
numberOfGoodTest = 0   
numberOfWrongTest = 0
for t,b in testSet:
  numberOfTest += 1
  if b == isNumberWithComa(t):    
    numberOfGoodTest +=1    
  else:
    print('Test Error:', t,  b)    
numberOfWrongTest = numberOfTest - numberOfGoodTest
print('Good Test:', numberOfGoodTest, '\nWrong Test:',  numberOfWrongTest)
