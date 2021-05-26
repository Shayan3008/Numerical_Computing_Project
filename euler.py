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
function = "e**(x-y)"
function = function.replace("e*", "E*")
# print(function)
func = sp.sympify(function)
i=a
ans = h*sp.N(func.subs(x, 0.5))
while True:
    if i==b:
        break
    ans = m+h*sp.N(func.subs(x, i).subs(y,m))
    print("value of y is :")
    print(ans)
    m = ans
    i+=0.5