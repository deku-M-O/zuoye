a=float(input("请输入需要转换的数字："))
yxs=int(input("请输入想要的小数位数："))
b=[]
xsl=[]
e=100
zs=int(a)
xs=a-zs
while e!=0:
    e=zs//2
    b.append(str(zs%2))
    zs=e
q=len(b)-1
for i in range(q//2):
    b[i],b[q-i]=b[q-i],b[i]
for h in range(yxs):
    xs=xs*2
    if xs>=1:
        xsl.append(str(1))
        xs=xs-1
    elif xs<1:
        xsl.append(str(0))
    elif xs==1:
        break
print(''.join(b)+"."+''.join(xsl))
#print(b[::-1])
b.split('.')