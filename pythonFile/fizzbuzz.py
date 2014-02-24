#for i in range(0,100):
#   if (i+1) % 3 == 0 and (i+1) % 5 == 0:
#       print i+1, "fizzbuzz"
#   elif (i+1) % 3 == 0:
#       print i+1,"fizz"
#   elif (i+1) % 5 == 0:
#       print i+1,"buzz"
for num in xrange(1,101):
    msg = ''
    if num % 3 == 0:
        msg += 'Fizz'
    if num % 5 == 0:
        msg += 'Buzz'
    print msg or num
