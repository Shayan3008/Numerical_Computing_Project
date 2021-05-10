import sympy as sp

print("Enter the lower limits:")
a = float(input())
b = float(input())
print("Enter the upper limit")
print("Enter the function:")
x = sp.symbols('x')
function = input()
func = sp.sympify(function)
h = b-a
print("The Ans Is\n")
first = h/2
ans = first*(sp.N(func.subs(x, a))+sp.N(func.subs(x, b)))
print(ans)
