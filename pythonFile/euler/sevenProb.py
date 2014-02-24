#answer 104743 
p=10001
i=0
n=0
primes = []
x=[]
while i < p:
    if n < 2: 
        n +=1
    elif n == 2:
        primes.append(n)
        n+=1
        i+=1
    elif n > 2 and n % 2 != 0:
        for j in range(2,n): 
            x.append(n%j==0)
        if any(x) == False:
            primes.append(n)
            i+=1
        n+=2
        x=[]
print primes
print x
