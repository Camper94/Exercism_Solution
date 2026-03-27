def equilateral(sides):
    s = 0
    r = False
    for d in sides:
        if s == d and s != 0: 
            s = d
            r = True 
        else: 
            s = d
            r = False
    return r

def isosceles(sides):
    s = sides[0]
    count= 0
    r = False
    for d in sides:
        if s == d: 
            count = count+1
            if count == 2: 
                r = True
    return r



def scalene(sides):
    pass


print(isosceles([1,1,3]))
