from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)
p = (x+2)*(y+3)
print(p)
(x + 2)*(y + 3)
p1=(x+2)*(y+3) + (x+2)*(x-3)
print(p1)

bieuthuc = x*x - x*y + y*y
giatri = bieuthuc.subs({x:3,y:x})
print(giatri)

giatri = bieuthuc.subs({x:3,y:3})
print(giatri)

giatri = bieuthuc.subs({y:x}).subs({x:3})
print(giatri)