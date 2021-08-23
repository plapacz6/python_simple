#
# date: 2021-08-23, autor: plapacz6@gmail.com
#
# excercise from https://automatetheboringstuff.com

import re

testSet = [
# regex,  test_regex, test_correct_date
# leap years
['29/02/1984', 1, 1],
['29/02/1985', 1, 0],
['29/02/2900', 1, 0], #divided by 100 but not by 400
['29/02/2800', 1, 1],

# number of month's days
['30/02/2021', 1, 0],
['31/02/2021', 1, 0],
['31/04/2021', 1, 0],
['31/06/2021', 1, 0],
['31/09/2021', 1, 0],
['31/11/2021', 1, 0],

# number of months
['31/00/2021', 1, 0],
['31/13/2021', 1, 0],
['31/59/2021', 0, 0],
['31/99/2021', 0, 0],

# corret date
['31/12/2021', 1, 1],

# format of date
['31_11-2021', 0, 0],
['31_11-2+21', 0, 0],
['31_11,2021', 0, 0],
['31_11-2a21', 0, 0],
['31_11-2021', 0, 0],
['31_11-2021', 0, 0],
['some--2021', 0, 0],
['31_11-2021', 0, 0],
['311-1-2021', 0, 0],
['_1_11-2021', 0, 0]
]

#TODO: checking the correctness of the numbers of days, months and leep years
def checkDate(text):
  correctDateRegex = r"""
  [0-3][0-9]\/[0-1][0-9]\/[1-2]\d\d\d
  """
  CDR_re = re.compile(correctDateRegex, re.VERBOSE)
  mo = CDR_re.search(text)
  if mo != None:
    if len(mo.group()) > 0 :
      print("found: ", mo.group())
      return True
  return False

testCounter = 0
testSuccess = 0
testFail = 0 
for d, te, td in testSet:
  testCounter += 1
  if bool(te) == checkDate(d):
    print("test ok: ", d)
    testSuccess += 1
  else:
    print("test FAIL: ", d, " expected :", bool(te), " get:" , checkDate(d))
    testFail += 1
print("Test Success: ", testSuccess)
print("Test Fail   : ", testFail)
