a=input("请输入二进制数字：")
b=0
a=a.split('.')
if int(len(a))==1:
    for i,j in enumerate(a[0]):
        b+=int(j)*2**(len(a[0])-1-i)
elif int(len(a))==2:
    for i,j in enumerate(a[0]):
        b+=int(j)*2**(len(a[0])-1-i)
    p=0
    for l,h in enumerate(a[1]):
        p+=int(h)*2**(-1-l)
    print(p+b)
else:
    print("错误")
