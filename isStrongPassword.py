#
# date: 2021-08-25, autor: plapacz6@gmai.com
# excercise from https://automatetheboringstuff.com
import re

#8 character lenth
#Upper and lower
#1 or more digit

testSet = [
['a3dbEgDa',1],
['abcefghikjslk', 0],
['abbdddkkkl3',0],
['D6ERRTGSDEW',0],
['Ab3',0],
['3344445544',0],
['DDWEEGIIYIIIR',0]
]

def isStrongPassword(p):
  #if len(p)<8 :
  #  return False
  re_8len = r".{8,}"
  re_UperLower = r"""
    (\w*[A-Z]\w*[a-z]\w*)
    |
    (\w*[a-z]\w*[A-Z]\w*)
    """
  re_1number = r"""
    \w*\d\w*
  """

  conditions = [
    {'desc': '8 char length',
      'def': 

    r".{8,}"

    },
    {'desc': 'Uppercase and lowercase letter',  
      'def': 
   
    r"""
    (\w*[A-Z]\w*[a-z]\w*)
    |
    (\w*[a-z]\w*[A-Z]\w*)
    """

    },
    {'desc': 'at least one digit', 
     'def': 

    r"""
    \w*\d\w*
    """

    }
  ]

  print()
  for condition in conditions:
    desc = condition["desc"]
    regexC =  re.compile(condition["def"],re.VERBOSE)
    mo = regexC.search(p)
    print('condition: "%(d)s :"'% {'d':desc}, end=" ")
    if mo != None:
      print(mo.group(), end=' <- ')
      print(' - OK')     
    else:
      print(', has not been met')
      return False    
  return True

testCounter = 0
testSucced = 0
testFailure = 0
for p, b in testSet:
  testCounter += 1
  if bool(b) == isStrongPassword(p):
    testSucced += 1
  else:
    testFailure += 1
print("Test succed :", testSucced)
print("Test failure:", testFailure)
