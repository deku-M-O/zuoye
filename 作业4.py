print(5*"*")
for i in range(3):
    print(1*"*"+3*(" ")+1*"*")
print(5*"*")

def fang(a):
    print(a*"*")
    for i in range(a):
        print(1*"*"+(a-2)*(" ")+1*"*")
    print(a*"*")
fang(8)