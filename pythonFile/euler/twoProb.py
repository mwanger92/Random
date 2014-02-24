sum = 0
num = 1
num2 = 2
while num2 < 4000000:
    if num2 % 2 == 0:
        sum += num2
    hold = num
    num = num2
    num2 = num + hold
print sum
