import sympy as sp

def forward(value,h,func):
    val=value+h
    a=sp.N(func.subs(x,val))
    b=sp.N(func.subs(x,value))
    c=(a+b)/h
    return c

points=[]
print("Enter the number of value:")
values=int(input())
print("1:Values and function values\n2:Values and function")
choice=int(input())
if(choice==1):
    print("w")
else:
    forwards=[]
    backward=[]
    print("Please enter values\n")
    for i in range(values):
        points.append(float(input()))
    print("Please enter function:")
    function=input()
    x=sp.symbols("x")
    func=sp.sympify(function)
    h=points[1]-points[0]
    hBack=h*(-1)
    for i in range(len(points)):
        forwards.append(forward(points[i],h,func))
        backward.append(forward(points[i],hBack,func))
    for i in range(len(points)):
        print(forwards[i])
        print(backward[i])
