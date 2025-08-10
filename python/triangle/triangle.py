def equilateral(sides):
    s = sides[0]
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
    for d in sides:
        if s == d: return True
        else: return equilateral(sides)



def scalene(sides):
    pass


print(equilateral([2,3,2]))
