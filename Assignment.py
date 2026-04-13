def f(x):
  d=0
  while x > 1:
    (x,d) = (x/2,d+1)
  return(d)
print(f(27182818))

def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
           s = s+i
    return(s)

print(h(60)-h(45))

def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return(res)

# for n in range(1,500):   # start from 1 to avoid division by zero
#     if g(375,n) == 4:
#         print(n)

print(g(375,4))