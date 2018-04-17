from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
i = Symbol('i')
j = Symbol('j')
k = Symbol('k')
t = Symbol('t')

def cross_product2(x,y):
    M = Matrix([[i,j],x,y])
    return M.det()

def cross_product3(x,y):
    M = Matrix([[i,j,k],x,y])
    return M.det()

def cross_productvec3(x,y):
    i = x[1]*y[2]-x[2]*y[1]
    j = x[2]*y[0]-x[0]*y[2]
    k = x[0]*y[1]-x[1]*y[0]
    return [i,j,k]

def norm(x):
    sumsquares = 0
    for i in range(0,len(x)):
        sumsquares = sumsquares+x[i]**2
    return (sumsquares)**0.5

def pointsdistance(x,y):
    sumsquares = 0
    for i in range(0,len(x)):
        sumsquares = sumsquares+(x[i]-y[i])**2
    return (sumsquares)**0.5

def pointsvector(x,y):
    vector = []
    for i in range(0,len(x)):
        vector.append(x[i]-y[i])
    return vector

def line_point(line,point):
    linesub1 = [(line[0].subs(t,1)),(line[1].subs(t,1)),(line[2].subs(t,1))]
    linesub0 = [(line[0].subs(t,0)),(line[1].subs(t,0)),(line[2].subs(t,0))]
    basevec = pointsvector(linesub1,linesub0)
    base = pointsdistance(linesub1,linesub0)
    return norm(cross_productvec3(pointsvector(point,linesub1),basevec))/base

line = eval(input('line = '))
point = eval(input('point = '))

print(line_point(line,point))



    
