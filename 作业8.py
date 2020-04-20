q=1
while q>0:
    a=int(input("请输入想要转换的数字："))
    b=int(input("请输入想要转换数字的单位(1.b;2.B;3.KB;4.MB;5.GB;6.TB)："))
    c=int(input("请输入想要转换的单位(1.b;2.B;3.KB;4.MB;5.GB;6.TB)："))
    if b>c:
        if c==1:
            w=a*(b-c-1)*1024
            if w==0:
                w=a*8
            else:
                w=w*8
        elif c!=1 and c<=6:
            w=a*(b-c)*1024
        else:
            print("输入错误！！(请输入序号)")
            q=q-1
        print(w)
        e=input("是(T)否(F)结束?")
        if e=="T":
            print("中止")
            q=q-1
        elif e=="F":
            print("继续")
        else:
            print("错误，中止")
            q=q-1
    elif b<c:
        if b==1:
            w=a/8
        elif b!=1 and b<=6:
            o=(c-b)*1024
            w=a/o
        else:
            print("输入错误！！(请输入序号)")
        print(w)
        e=input("是(T)否(F)结束?")
        if e=="T":
            print("中止")
            q=q-1
        elif e=="F":
            print("继续")
        else:
            print("错误，中止")
            q=q-1