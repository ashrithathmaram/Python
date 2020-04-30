#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
def g(a):
    for val in range(2, a):
        y = float(float(a)/val)
        if (y == int(y) and y > 1):
            return True
            break
        else:
            return False
def f(x):
    counter = 1
    list_1 = []
    while counter <= x:
        if x % counter == 0:
            if g(counter):
                list_1.append(counter)
        counter += 1
    return list_1
