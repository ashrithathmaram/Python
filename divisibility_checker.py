print "DIVISIBILITY CHECKER"
try:
  y = int(raw_input("Enter the divisor for which you want to check divisbility: "))
  x = int(raw_input("Enter your dividend for divisibility here: "))
  if x % y == 0:
    print "Your number is divisible by " + str(y)
  else:
    print "Your number is not divisible by " + str(y)
except ValueError:
  print "Please enter a numerical value"
