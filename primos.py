n = 542
for i in range(1, n+1):
    divisores = 0
    for div in range(1, i+1):
        if i %div == 0:
            divisores +=1
    if divisores == 2:
            print(i)
