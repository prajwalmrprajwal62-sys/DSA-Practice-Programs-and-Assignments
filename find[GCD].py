def gcd(m,n):   # 1 way to find GCD
    fm =[]
    for i in range(1,m+1):
        if (m%i)==0:
            fm.append(i)

    fn = []
    for j in range(1,n+1):
        if (n%j)==0:
            fn.append(j)

    cp =[]
    for f in fm:
        if f in fn:
            cp.append(f)
    print(cp[-1])

gcd(58,96) 

# 2 Ways to find GCD
def gcd2(p,q):
    while(q):
        p,q = q, p%q
    return p
print(gcd2(58,96))

# 3 Ways to find GCD
def gcd3(a,b):
    cf =[]
    for i in range(1,min(a,b)+1):
        if (a%i)==0 and (b%i)==0:
            cf.append(i)
    return cf[-1]
print(gcd3(58,96))

def gcd4(x,y):   # 4 Ways to find GCD
    if y==0:
        return x
    else:
        return gcd4(y, x%y)
print(gcd4(58,96))

def gcd5(c,d):
    for i in range(min(c,d),0,-1):
        if (c%i==0) and (d%i==0):
            mcf= i
            return mcf   #  OR use return i directly no need of mcf variable
    
print(gcd5(58,96))

def gcd6(u,v):
    for i in range(min(u,v),0,-1):
        if (u%i==0) and (v%i==0):
            return i
        
print(gcd6(58,96))

# by while loop
def gcd7(s,t):
    i=min(s,t)
    while i>0:
        if (s%i==0) and (t%i==0):
            return i
        else:
            i=i-1

print(gcd7(58,96))
        
def gcd8(e,f):
    while e!=f:
        if e>f:
            e=e-f
        else:
            f=f-e
    return e
print(gcd8(58,96))

def gcd9(g,h):
    if g<h:
        (g,h)=(h,g)
        if (g%h)==0:
            return h
        else:
            diff =g-h
            return gcd9(min(h,diff), max(h,diff))
        
print(gcd9(58,96))

def gcd10(j,k):
    # if j<k:
    #     (j,k)=(k,j)
    while (j%k)!=0:
        j,k = k, j%k
    return k

print(gcd10(96,58))