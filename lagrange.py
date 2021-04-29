import sympy as sp

from math import log as ln


def Lagrange(lists, j, solvedFunc):
    return (lists/j)*solvedFunc

pointStored = []
x = sp.symbols('x')
function = input()
function = function.replace("e**", "E**")
symFunction = sp.sympify(function)
print("Enter main point:")
point = int(input())
print("Enter the no of points you want to Enter:")
count = int(input())
print("Enter the "+str(count)+" points:")
for i in range(count):
    pointStored.append(float(input())+0.0)
ans = 0.0
temp3=1
temp4=1
for i in range(count):
    solFunc = sp.N(symFunction.subs(x, pointStored[i]))
    for j in range(count):
        if(i != j):
            temp1=point-pointStored[j]
            temp2=pointStored[i]-pointStored[j]
            temp3=temp3*temp1
            temp4=temp4*temp2
    ans = ans+Lagrange(temp3, temp4, solFunc)
    temp3=1
    temp4=1
print(ans)