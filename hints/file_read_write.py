
 
with open('test.txt', 'r') as f:
  #praca w w bloku
  #automatycznei zamyka plik
  #pass
  #f_contents = f.read()
  #f_line = f.readline()
  #print(f_contents)
  #print(f_line)
  #print(f_line, end='')
  #for line1 in f:  
  #print(line1, end='')
  size_to_read = 10
  f_const2 = f.read(size_to_read)
  while len(f_const2) > 0:
    print(f_const2, end='*')
    print(f.tell(), end="*")
    f_const2 = f.read(size_to_read)
    #f.seek(0)
  
#print(f.name, f.mode)


#f = open('test.txt', 'r') #'w' 'a' 'r+"     binarne: "rb" "wb"
#trzeba pamietac o zamknieciu ppliku
#f.close()

#  ------------   WRITE -------------------

with open("test2.txt", "w") as f:
  f.write('zapis do pliku test2.txt')

