print "Input a number 'n' to find the sum of the first 'n' natural numbers"
try:
  n = int(raw_input("Number: "))
  x = 0
  for val in range(1, n+1):
    x = x + val
  print x
except ValueError:
  print "Please input a number"


print "Input a number 'n' to find the sum of the first 'n' natural numbers"
try:
  n = int(raw_input("Number: "))
  x = (n+1) * (.5*n)
  print int(x)
except ValueError:
  print "Please input a number"