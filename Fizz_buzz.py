print "Fizz or Buzz?"
try:
  x = int(raw_input("Number: "))
  if (x % 3 == 0 and x % 5 == 0):
   print "FizzBuzz"
  else:
   if x % 3 == 0:
    print "Fizz"
   if x % 5 == 0:
    print "Buzz"
except ValueError:
  print "Please input a number"