print "FIBONACCI PRINTER"
def f(x):
  if x == 2:
    return 1
  else:
    if x == 1:
      return 0
    else:
      return f(x-2) + f(x-1)
try:
  y = int(raw_input("How many numbers of the Fibonacci Sequence? "))
  if y < 0:
   print "Please enter a whole number"
  else:
   x = 1
   while x < y + 1:
     print f(x)
     x += 1
except ValueError:
  print "Please enter a whole number"