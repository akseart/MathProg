u"""

"""
import numpy
import sympy
import numexpr as ny
x, y, z = sympy.symbols('x y z')
func = "5*x**2+3*y**2+2*z**2+2*x*y-y*z+10*x-4*z"


def f(V):
    " " " return value function " " "
    x, y, z = V
    return (eval(func))


def grad(Xk):
    ex = sympy.diff(func, x)
    ey = sympy.diff(func, y)
    ez = sympy.diff(func, z)
    exd = ex.subs([(x, Xk[0]), (y, Xk[1]), (z, Xk[2])])
    eyd = ey.subs([(x, Xk[0]), (y, Xk[1]), (z, Xk[2])])
    ezd = ez.subs([(x, Xk[0]), (y, Xk[1]), (z, Xk[2])])
    ag = numpy.array([exd, eyd, ezd])
    ag = ag
    return (ag)


# Градиентный спуск с дроблением
def gradient_descent(f, xk, grad, eps, step, max_steps):
    xk1 = xk
    for i in range(max_steps):
        xk1 = xk + (step * grad(xk))
        print (i, xk1)
        if f(xk1) >= f(xk):
            step = step / 4
            continue
        if not numpy.linalg.norm((xk1-xk), ord=1) > eps:
            break
        xk = xk1
    return xk1


# Одномерная оптимизация
# Метод наискорейшего спуска
def fastest_descent(f, xk, grad, eps, step, max_steps):
    xk1 = xk
    i = 0
    ag = grad(xk)
    for i in range(max_steps):
        xk1 = xk + (step * ag)

        print (i, xk1)
        i = i+1
        if (f(xk1) >= f(xk)) and i == 0:
            step = step / 4
            i = 0
            xk = xk1
            continue
        if (f(xk1) >= f(xk)) and i > 0:
            ag = grad(xk)
            i = 0
            xk = xk1
            continue
        if not step > eps:
            break
        xk = xk1
    return xk1


xk = numpy.array([-1., 0.5, 1.])
print (xk)
eps = 0.000000000000001
print ("!!!")
step = 0.5
print (gradient_descent(f, xk, grad, eps, 0.5, 1000))
print (-119./107, 60./107, 122./107)
eps = 0.001
xk = numpy.array([-1.11, 0.56, 1.14])
print (fastest_descent(xk))
print (-119./107, 60./107, 122./107)
