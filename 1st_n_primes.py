print "Enter a number(n) to find the first 'n' prime  numbers"
repeat = 1
while repeat == 1:
  f = 1
  try:
    n = int(raw_input("Number: "))
    a = 2
    b = 1
    while b <= n:
      c = 1
      for z in range(2, a):
       y = float(a)/z
       if y == int(y):
         c *= 0
         break
      if c == 1:
       print a
       b += 1
      a += 1
  except ValueError: 
    print "Please enter a valid number"
  while f == 1:
   ans = str(raw_input("Restart? Enter yes or no: "))
   if ans == "yes":
     repeat = 1
     f = 0
   else:
     if ans == "no":
       repeat = 0
       f = 0
       print "Goodbye!"
     else:
       print "Wrong input. Please enter yes or no"
       repeat = 0