n=100
sumSquared = 0
squareSum = 0
for i in range(0,n):
    squareSum+=(i+1)
squareSum = squareSum*squareSum
for i in range(0,n):
    sumSquared+=(i+1)*(i+1)
print squareSum-sumSquared
