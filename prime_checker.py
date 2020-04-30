print "Is it a prime number?"
try:
  x = int(raw_input("Number: "))
  for val in range(2, x):
   y = float(float(x)/val)
   if (y == int(y) and y > 1):
     print "This number is not prime"
     break
  if (x != 1 and x != 0 and x > 1):
   print "This number is prime"
  else:
   print "This number is not prime"
except ValueError:
  print "Please input a number"
  
