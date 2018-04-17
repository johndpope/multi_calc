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

def hessianmatrix(func):
    return diff(diff(func,x),x)*diff(diff(func,y),y)-diff(diff(func,y),x)*diff(diff(func,x),y)
    
def localmaxmin(critical_point,func):
    if hessianmatrix(func).subs([(x,critical_point[0]),(y,critical_point[1])]) < 0:
        print('%s is a saddle point'% critical_point)
    else:
        if diff(diff(func,x),x).subs([(x,critical_point[0]),(y,critical_point[1])]) > 0:
            print('%s is a local min'% critical_point)
        else:
            print('%s is a local max'% critical_point)

    
def critical_points(func):
    critical_points = list(nonlinsolve([partial_x(func,x),partial_y(func,y)],[x,y]))
    return critical_points

def critical_points_check(func):
    for i in range(0,len(critical_points(func))):
        localmaxmin(critical_points(func)[i],func)
    

func = eval(input('f(x) = '))

critical_points_check(func)





