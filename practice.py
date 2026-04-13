def mystry(l,v):
    if len(l)==0:
        return v
    else:
        return mystry(l[:-1], l[-1]+v)
    
print(mystry([],7))

def mystry2(l,v):
    if len(l)==0:
        return v
    else:
        return mystry2(l[:-1], l[-1]*v)
    
print(mystry2([2,3,4,6],7))

def refree(s):
    seen =set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

print(refree("heloo"))