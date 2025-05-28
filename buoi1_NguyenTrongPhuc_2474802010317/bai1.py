from sympy import Symbol, solve
x = Symbol('x')
bieuthuc = x + 3 - 5
print(solve(bieuthuc))

bieuthuc = x**2 + 3 - 5
nghiemx = solve(bieuthuc)
print(nghiemx)

print(nghiemx[0])

print(nghiemx[1])