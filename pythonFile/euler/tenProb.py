num=2000000
i=0
sum = 0
primes=[]
x=[]
while i < num:
    if i < 2:
        i += 1
    elif i == 2:
        primes.append(i)
        i+=1
    elif i > 2 and i%2!=0:
        for j in range(2, i):
            x.append(i%j==0)
        if any(x) == False:
            primes.append(i)
            i+=1
        x=[]
        i+=1
for i in range(0,len(primes)):
    sum+=primes[i]
print sum
