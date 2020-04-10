a=int(input("请输入需要转换的数字："))
b=[]
e=100
while e!=0:
    e=a//2
    b.append(a%2)
    a=e
b[0],b[len(b)-1]=b[len(b)-1],b[0]
b[len(b)//2-1],b[len(b)//2+1]=b[len(b)//2+1],b[len(b)//2-1]
print(b)
#print(b[::-1])