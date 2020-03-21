def os(a,b):
    a=[]
    for i in range(a,b+1):
        if i%2==0:
            a.append(i)
    print(a)
os(1,100)