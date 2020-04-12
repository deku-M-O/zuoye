a=float(input("请输入需要转换的数字："))
b=[]
e=100
zs=int(a)
xs=a-zs
while e!=0:
    e=zs//2
    b.append(a%2)
    zs=e
q=len(b)-1
for i in range(q//2):
    b[i],b[q-i]=b[q-i],b[i]
print(b)
#print(b[::-1])