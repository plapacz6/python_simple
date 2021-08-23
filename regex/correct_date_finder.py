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

def checkDate(text):
  correctDateRegex = r"""
  ([0-3][0-9])\/([0-1][0-9])\/([1-2]\d\d\d)
  """
  CDR_re = re.compile(correctDateRegex, re.VERBOSE)
  mo = CDR_re.search(text)
  match = False
  correct = False
  if mo != None:
    if len(mo.group()) > 0 :
      print("found: ", mo.group())
      match = True
      
      #checking month and number of days
      month = int(mo.group(2))
      days = int(mo.group(1))
      years = int(mo.group(3))
         
      leapYear = False              
      if years%4 == 0:
        if years%100 == 0:
          if years%400 == 0:
            leapYear = True
          else:
            leapYear = False
        else:
          leapYear = True
  
      if month > 0 and month < 13: 
        if month in [1,3,5,7,8,10,12]: 
        #1 or month = 3 or month = 5 or month = 7 or month = 8 or month = 10 or month = 12:
           if days >= 1 and days <= 31:
             correct = True
             return (match, correct)
        if month in [4,6,9,11]: 
        #== 4 or mouth == 6 or mouth == 9 or mouth == 11:
          if days >= 1 and days <= 30:
            correct = True
            return (match, correct)
        if month == 2:
           if leapYear:
              if days >= 1 and days <= 29:
                correct = True               
                return (match, correct)
           else:
             if days >= 1 and days <= 28:
               correct = True               
               return (match, correct)            
  return (match, correct)

testCounter = 0
testSuccess = 0
testFail = 0 
print("test: regex match")
for d, te, td in testSet:
  testCounter += 1
  if bool(te) == checkDate(d)[0]:
    print("test ok: ", d)
    testSuccess += 1
  else:
    print("test FAIL: ", d, " expected :", bool(te), " get:" , checkDate(d)[0])
    testFail += 1
print("Test Success: ", testSuccess)
print("Test Fail   : ", testFail)

print("test correctness of date")
for d, te, td in testSet:
  testCounter += 1
  if bool(td) == checkDate(d)[1]:
    print("test ok: ", d)
    testSuccess += 1
  else:
    print("test FAIL: ", d, " expected :", bool(td), " get:" , checkDate(d)[1])
    testFail += 1
print("Test Success: ", testSuccess)
print("Test Fail   : ", testFail)
