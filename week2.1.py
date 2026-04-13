l = [2,3,4,8,9,7]

def update(l,i,v):
    if i>0 and i<len(l):
        l[i]=v
        return True
    else:
       
        v=v+1
        return False


print(update(l,7,12))
print(l)


