# modified euler method
# k1=hf(ti,wi)
# k2=hf(ti+1,wi+k1)
# wi+1=wi+1/2(k1+k2)

import sympy as sp
from math import log as ln

print("Enter the lower limits:")
a = float(input())
print("Enter the upper limit")
b = float(input())
print("enter the value of h")
h = float(input())
print("enter the initial value of t and the y value")
c = float(input())
m = float(input())
print("value of y is:")
print(m)
x = sp.symbols('x')
y = sp.symbols('y')
function = "(1+x)/(1+y)"
function = function.replace("e*", "E*")
print(function)
func = sp.sympify(function)
i=a

while True:
    if i==b:
        break
    k1 = h*sp.N(func.subs(x, i).subs(y,m))
    k2 = h*sp.N(func.subs(x,i+h).subs(y,m+k1))
    answer = m + (1/2*(k1+k2))
    print("value of y is :")
    print(answer)
    m = answer
    i+=0.5