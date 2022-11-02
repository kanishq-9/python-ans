import re
def check(a):
    x=re.search("(.*aaa.*)|(.*bbb.*)",a)
    if x:
        return True
    return False
def con(a,val,i):
    k=a[:i]+val+a[i+1:]
    return k

a=(input())
if check(a):
    print("not")
else:
    for i in range(len(a)): 
        if a[i]=="?":
            
            a=con(a,"a",i)
            if not check(a):
                continue
            else:
                a=con(a,"b",i)
                continue

        else:
            pass
if not check(a):
    print(a)
            
