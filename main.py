a = int(input()) # Ax^2+Bx+C=0
b = int(input())
c = int(input())
D = b**2 - 4*a*c
if D < 0:
    print("Корней нет")
elif D == 0:
    x = -b/(2*a)
    print("x=", x, "- корень уравнения")
else:
    x1 = (-b + D**0.5)/(2*a)
    x2 = (-b - D**0.5)/(2*a)
    print("x1 =", x1, "и x2 =", x2, "- корени уравнения")