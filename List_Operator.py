print "List Operator"
print "First, you need to create your list"
Pass = 0
add_counter = 1
main_list = []
while Pass == 0:
  counter = raw_input("How many elements will your list have?" )
  try:
    if counter > 0:
      if float(counter) == int(counter):
        Pass = 1
      else:
        print "Please enter a natural number"
    else:
      print "Please enter a natural number"
  except ValueError:
    print "Please enter a natural number"
while add_counter <= int(counter):
  main_list.append(raw_input("Enter element: "))
  add_counter += 1
print "Here is your completed list: "
print main_list
