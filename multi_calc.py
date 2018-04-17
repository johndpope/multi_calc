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
    if len(x) != len(y):
        print('You cannot dot 2 vectors of different dimensions')
    else:
        scalar_final = 0
        for i in range(0,len(x)):
            scalar_final = scalar_final + x[i] * y[i]
        return (scalar_final)

def cross_product2(x,y):
    M = Matrix([[i,j],x,y])
    M
    return M.det()

def cross_product3(x,y):
    M = Matrix([[i,j,k],x,y])
    M
    return M.det()

def level_tangent(func,point):
    minuspoint = []
    for i in range(0,len(point)):
        minuspoint.append(x-point[i])
    
    if len(point) == 2:
        func.subs([(x,point[0]),(y,point[1])])
        #return(dot_product(gradient2(func),minuspoint))
        equation = '%s = 0' % (dot_product(gradient2(func),minuspoint))
        print (equation)
    else:
        func.subs([(x,point[0]),(y,point[1]),(z,point[2])])
        #return(dot_product(gradient3(func),minuspoint))
        equation = '%s = 0' % (dot_product(gradient3(func),minuspoint))
        print (equation)






