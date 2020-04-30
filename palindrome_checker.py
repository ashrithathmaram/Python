print "Is it a palindrome?"
try:
 x = raw_input("String: ")
 l = len(x)
 for val in range(0, int(l/2)+1):
   if x[val] != x[l-(val+1)]:
     print "No"
     quit()
 print "Yes"
except ValueError:
 print 'Please enter a valid response'