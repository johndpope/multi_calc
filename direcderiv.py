from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
i = Symbol('i')
j = Symbol('j')
k = Symbol('k')

def partial_x(func,x):
    return (diff(func,x))

def partial_y(func,y):
    return (diff(func,y))

def partial_z(func,z):
    return (diff(func,z))

def gradient2(func):
    return [partial_x(func,x), partial_y(func,y)]

def gradient3(func):
    return [partial_x(func,x), partial_y(func,y), partial_z(func,z)]

def dot_product(x,y):
    scalar_final = 0
    for i in range(0,len(x)):
        scalar_final = scalar_final + x[i] * y[i]
    return (scalar_final)

def direcderiv(func, point, direc):
    if len(point) == 2:
        g = [gradient2(func)[0].subs([(x,point[0]),(y,point[1])]),gradient2(func)[1].subs([(x,point[0]),(y,point[1])])]
    else:
        g = [gradient3(func)[0].subs([(x,point[0]),(y,point[1]),(z,point[2])]),gradient3(func)[1].subs([(x,point[0]),(y,point[1]),(z,point[2])]),gradient3(func)[2].subs([(x,point[0]),(y,point[1]),(z,point[2])])]

    

    return dot_product(g,direc)

func = eval(input('f(x) = '))
point = eval(input('P = '))
direc = eval(input('u = '))

print (direcderiv(func, point, direc))
    
