def istriangle(sides):
    return any(sides) and sum(sides) > 2*max(sides)

def equilateral(sides):
    return istriangle(sides) and len(set(sides)) == 1 

def isosceles(sides):
    return istriangle(sides) and ((equilateral(sides)) or len(set(sides)) == 2)

def scalene(sides):
    return istriangle(sides) and len(set(sides)) == 3


