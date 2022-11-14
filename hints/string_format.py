#dictionary
person = {'name': 'Tom', 'age': 23}

sentence1 = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) +  ' years old.'

sentence2 = 'My name is {} and I am {} yars old'.format(person['name'],person['age'])

sentence = 'My is {0} and I am {1}'.format(person['name'],person['age'])

sentence = '<{0}>{1}</{0}>'.format('h1','moj tekst')

sentence = 'My {0[name]} and {0[age]}'.format(person)
sentence = 'My {0[name]} and {1[age]}'.format(person, person)

#list
l = ['Ann',23]
sentence = 'My {0[0]} and {0[1]}'.format(l)


#class
class Person1():
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person1('Jack', '33')

sentence = 'My is {0.name} and I am {0.age}'.format(p1)

#key word arguments
sentence = 'My is {name} and I am {age}'.format(name='Olga',age='30')

#depacking dictionary
sentence = 'My is {name} and I am {age}'.format(**person)

print(sentence) 


#formating numbers
for i in range(1, 11):
  #sent2 = 'The value is {}'.format(i)
  sent2 = 'The value is {:02}'.format(i)
  print(sent2)
pi = 3.14159265

sent2 = 'The PI value is {:.3f}'.format(pi)

#big value
sent2 = 'The BIG value is {:.3f}'.format(1000**2)

#date time
import datetime
my_date = datetime.datetime(2015, 9, 24, 12, 30, 45)
print(my_date)
sent2 = 'The DATA TIME value is {:%B %d, %Y}'.format(my_date)
sent2 = '{0:%B %d, %Y} wypada {0:%A} i byl to {0:%j} dzien roku'.format(my_date)


print(sent2)



