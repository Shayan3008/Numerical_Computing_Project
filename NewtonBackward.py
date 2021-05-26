import sympy as sp
mainCount = 1
list1 = []  # values of x
list2 = []  # values of fx
list3 = []  # value of a0,a1,a2
list4 = []
x = sp.symbols('x')
#unction = "2*x"
print("do u want to give values of f(X) or give a function\n")
decis = int(input("1-value of fx   2-function "))
if(decis == 2):
    print("Enter the Function:")
    function = input()
val = int(input("enter how many value of x to be inserted\n"))
for i in range(val):
    k = float(input("enter values of x \n"))
    list1.append(k)
    if(decis == 1):
        functionvalue = float(input("enter value of fx"))
        list2.append(functionvalue)
    elif(decis == 2):
        symFunction = sp.sympify(function)
        solFunc = sp.N(symFunction.subs(x, k))
        list2.append(solFunc)
list1.reverse()
list2.reverse()
list3.append(list2[0])

temp = val
while (val > 1):
    for i in range(val-1):
        if(i == 0):
            a = list2[i+1]-list2[i]
            list3.append(a)
            list2[i] = a
        else:
            a = list2[i+1]-list2[i]
            list2[i] = a
    mainCount += 1
    val -= 1

for i in range(len(list3)):
    print(list3[i])

# x = 0.0
# print("Enter the function value :")
# func = float(input())
# print("P" + str(temp-1) + " = ")
# for i in range(temp-1):
#     c = 1.0
#     if(i == 0):
#         x += list3[i]
#     elif(i > 0):
#         j = i-1
#         while(j >= 0):
#             c = c*(func-list1[j])
#             j -= 1
#         k = list3[i]*c
#         x += k
# print(x)