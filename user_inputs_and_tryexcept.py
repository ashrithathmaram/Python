number_a = raw_input("Enter First Number: ")
number_b = raw_input("Enter Second Number: ")

try:
    sum_ab = int(number_a) + int(number_b)
    print sum_ab
except ValueError:
    print "Please enter a numerical value"

