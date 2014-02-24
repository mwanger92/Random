list = []
for i in range(999,-0,-1):
    for j in range(999,-1,-1):
        x=i*j
        x=str(x)
        y = x[::-1]
        if x == y:
            list.append(int(x))
            break
print max(list)
