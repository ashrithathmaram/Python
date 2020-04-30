number = raw_input("Enter your number here: ")
try:
  x = int(number)
  if x % 2 == 1:
      print "Your number is odd"
  else:
      print "Your number is even"
except ValueError: 
  print "Please enter a numerical value"
  
#Homework challenge: Write number to check for prime number