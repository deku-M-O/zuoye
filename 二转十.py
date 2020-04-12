a=input("请输入二进制数字：")
b=0
for i,j in enumerate(a):
    b+=(int(j)*2**i)
print(b)