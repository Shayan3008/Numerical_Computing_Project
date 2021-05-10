import sympy as sp

def forwardDiff(func,index,list,h):
    a=list[index]+h
    if a in list:
        indexs=list.index(a)
        return (func[indexs]-func[index])/h
    else:
        return "Not Possible at this index"

# def backwardDiff(func,index,list,value,h):

def forward(value, h, func):
    val = value+h
    a = sp.N(func.subs(x, val))
    b = sp.N(func.subs(x, value))
    c = (a-b)/h
    return c


points = []
print("Enter the number of value:")
values = int(input())
print("1:Values and function values\n2:Values and function")
choice = int(input())
if(choice == 1):
    forwards = []
    backward=[]
    functionVal=[]
    print("Please enter values and functions\n")
    for i in range(values):
        points.append(float(input()))
        functionVal.append(float(input()))
    h=points[1]-points[0]
    hBack=h*(-1)
    forwardDiff(functionVal,0,points,h)
    for i in range(len(points)):
        forwards.append(forwardDiff(functionVal,i,points,h))
        backward.append(forwardDiff(functionVal,i,points,hBack))
    for i in range(len(points)):
        print(forwards[i])
        print(backward[i])
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
