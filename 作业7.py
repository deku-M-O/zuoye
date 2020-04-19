a=input("请输入需要转换反码的二进制数字：")
b=list(a)
for i in range(len(b)):
    if b[i]=='0':
        break
    elif b[i]=='1':
        if b[i+1]=='1':
            b[i+1]='0'
        elif b[i+1]=='0':
            b[i+1]='1'
print(''.join(b))