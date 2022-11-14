
#vovel -> +"yay"
#consonant or consonant cluster -> ...cluster + ay

tests = [
('My name is AL SWEIGART and I am 4,000 years old.',
'Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.', 1),
('you are chess master', 
'youyay areyay esschay astermay', 1)
]

def pigLatinTranslator(text):
  vovels = 'aeiouy'
  text = text.strip()
  text1 = text.split(' ')
  isUpper = False
  isTitle = False
  text2 = ''
  for expr in text1:
    if expr[0].isdigit():
      pass
    else:
      isUpper = expr.isupper()
      isTitle = expr.istitle()
      expr = expr.lower()
      if expr[0] in vovels:
        expr = expr + 'yay'
      else:
          if len(expr) > 1:
            if expr[1] in vovels:
              expr = expr[1:] + expr[0] + 'ay'              
            else:
              expr = expr[2:] + expr[0] + expr[1] + 'ay'
          else:
            expr = expr[1:] + expr[0] + 'ay'
      if isUpper:
        expr = expr.upper()
      if isTitle:
        expr = expr.title()
    text2 += ' ' + expr
  #text2 = ' '.join(text1)
  text2 = text2.strip()
  return text2
  

test_ok = 0
test_NOTok = 0

for test in tests:
  if test[2] == 1:
    if test[1] == pigLatinTranslator(test[0]):
      test_ok += 1
    else:
      print("test : ", test, "not passed")
      print(" : ", pigLatinTranslator(test[0]))      
      test_NOTok +=1
  else:
    if test[1] != pigLatinTranslator(test[0]):
      test_ok += 1
    else:
      print("test : ", test, "not passed")
      print(" : ", pigLatinTranslator(test[0]))
      test_NOTok +=1    
print(test_ok, " tests succeed")
print(test_NOTok, " tests failed")

