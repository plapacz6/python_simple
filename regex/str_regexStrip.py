#
# date: 2021-08-26, autor:plapacz6@gmail.com
# excercise from https://automatetheboringstuff.com

#str.strip() method with regex second argment

import re

testSet = [
["43BB%some test both end43BB%", "some test both end", "43BB%", 1],
["some test on the right43BB%", "some test on the right", "43BB%", 1],
["43BB%some test on the left", "some test on the left", "43BB%", 1],
["some test 43BB% in the middle", "some test 43BB% in the middle", "43BB%", 1],
["some test without", "some test without", "43BB%", 1],
["43BB%some test 43BB% in the middle and left", "some test 43BB% in the middle and left", "43BB%", 1],
["some test 43BB% in the middle and right43BB%", "some test 43BB% in the middle and right", "43BB%", 1],
["some test without", "some test without", "", 1],
["  some test without  ", "some test without", "", 1],

["43BB%some test both end43BB%", "43BB%some test both end43BB%", "43BB%", 0],
]

def str_regexStip(s, regex = ""):
  if regex == "":
    return s.strip()
  regexA = '^(' + regex  + ')'
  regexB = '(' + regex  + ')$'

  regexC = re.compile(regexA) 
  sM = regexC.sub('', s)
  regexC = re.compile(regexB)
  sM = regexC.sub('', sM)
  return sM


testSucced = 0
testFailure = 0
testCounter = 0
for t, w, r, b in testSet:
  testCounter += 1
  if  str_regexStip(t, r) == w:
    if bool(b):
      testSucced += 1   
    else:
      testFailure += 1
  else:
    if not bool(b):
      testSucced += 1   
    else:
      testFailure += 1
print("Test Succed : ", testSucced)
print("Test Failure: ", testFailure)

  
  
