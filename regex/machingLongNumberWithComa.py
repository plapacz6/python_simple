#
# date: 2021-08-20, autor: plapacz6@gmail.com

import regex
testSet = [
  ['12', 1],
  ['446', 1],
  ['1,454' 1],
  ['34,989'' 1],
  ['994,431', 1],
  ['4,233,210',1],
  ['99,234,219', 1],
  ['434,200,871', 1],
  ['4,991,090,234', 1]
  ['452434', 0],
  [56,8824', 0],
  ['98,44,799', 0]
]

def isNumberWithComa(n):
  reNumWithComa = r'('d{3},)*(\d{0,3}?)'
  objReNWC = re(reNumWithComa)
  if len(objReNWC.group() > 0):
    return True
  return False

numberOfTest = 0
numberOfGoodTest = 0   
for r,b in testSet:
  numberOfTest += 1
  if b == and isNumberWithComa(t):    
    numberOfGoodTest +=1    
  else:
    print('Test Error: %s, %s', r, b)
print('Good Test: %s, \nWrong Test: %s\n', numberOfGoodTest, numberOfTest-numberOfGoodTest)
 
