from pathlib import Path
import sys
import hashlib
import os
#parse cmd line parameters
#- file with searched phrases
#- http url
#- max number of results
args1 = ""
if __name__ == "__main__":
  try:
    args1 = sys.argv[1]  #may raise exception
    args = sys.argv      #preparing on events like : sys.argv.pop()
    if len(sys.argv) < 2:   
      #print(f"\nusage: {sys.argv[0]=} file_with_phrase  url \n")  #since 3.8
      print(f"\nusage: {sys.argv[0]} file_with_phrase  url \n")
    else:
      print(f"number of arguments: {len(sys.argv)}")
      for i, arg in enumerate(sys.argv):
        print(f"Arg nr {i:>6}: {arg}")
    print(f"{sys.argv[1:]}")
    print(f"{sys.argv[::-1]}")  
  except IndexError: 
    raise SystemExit(f"\nexcept: usage: {sys.argv[0]} file_with_phrase  url \n")
else:
  exit(0);

#sha1sum of arg 1
m = hashlib.sha1()  #instatiation of sha1 arlgoritm
m.update( bytes(args1, 'utf-8')) #update sha1 obj w
                                 #ith bytes version of sring in arg1

m2 = hashlib.sha1()
m2.update( os.fsencode(sys.argv[1])) #os bytes representation of argv1

print(m.hexdigest())
print(m2.hexdigest())            #hex printout of sha1(arg1)




#open file with searched phrases
#print(type(Path('~','my_app','app')))
print(str(Path('~','my_app','app')))


#write results


#close files


