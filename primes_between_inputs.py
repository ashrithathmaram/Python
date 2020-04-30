print "Enter any two whole numbers to find all prime numbers between them"
repeat = True
while repeat:
  y_or_n_repeat = True
  try:
    n = int(raw_input("Starting Number: "))
    end = int(raw_input("Ending Number: "))
    if n > end:
      print "Your first number should be smaller than your second number"
    else:
      no_prime = True
      while n <= end:
        no_factors = True
        for factor in range(2, n):
          y = float(n)/factor
          if y == int(y):
            no_factors = False
            break
        if no_factors and n > 1:
          print n
          no_prime = False
        n += 1
      if no_prime:
        print "There are no prime numbers between your two inputs"
  except ValueError:
    print "Please enter a valid number"
  while y_or_n_repeat:
   ans = str(raw_input("Restart? Enter yes or no: "))
   if ans == "yes":
     repeat = True
     y_or_n_repeat = False
   else:
     if ans == "no":
       repeat = False
       y_or_n_repeat = False
       print "Goodbye!"
     else:
       print "Wrong input. Please enter yes or no"
       repeat = False