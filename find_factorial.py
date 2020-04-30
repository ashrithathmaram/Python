def fac(x):
  y = 1
  while x > 0:
    y *= x
    x -= 1
  if x > -1:
    print y