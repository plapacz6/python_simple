#https://realpython.com/python-command-line-arguments/#a-few-methods-for-parsing-python-command-line-arguments

import sys

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-c" in opts:
  print(" ".join(arg.capitalize() for arg in args))
elif "-u" in opts:
  print(" ".join(arg.upper() for arg in args))
elif "-l" in opts:
  print(" ".join(arg.lower() for arg in args))
else:
  #maybe require > 3.6
  #raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")
  pass

