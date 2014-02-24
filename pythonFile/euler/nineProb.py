mustEqual = 1000

for a in range(1,mustEqual+1):
    for b in range(1,mustEqual+1):
        for c in range(1,mustEqual+1):
            if a < b < c and a + b + c == 1000 and (a*a) + (b*b) == (c*c):
                print (a*b*c) 
