number=10
def falsify(list):
    for i in range(0,number):
        list[i]=False

list = [False]
list*=number
n=1
while all(list) == False:
    falsify(list)
    for i in range(1,number+1):
        if n % i == 0:
            list[i-1]=True
    n+=1
print n-1
