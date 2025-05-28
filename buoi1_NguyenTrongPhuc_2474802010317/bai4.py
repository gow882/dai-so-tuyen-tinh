from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
pt1 = 2*x+3*y-12
pt2 = 3*x-2*y-5

solve((pt1, pt2), dict=True)

nghiem = solve((pt1, pt2), dict=True)
nghiem = nghiem[0]
a= pt1.subs({x:nghiem[x], y:nghiem[y]})
b= pt2.subs({x:nghiem[x], y:nghiem[y]})
print(a)
print(b)