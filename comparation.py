a = 12
b = 6

result = a > 10
print(a,'>',10,'=', result)
result = b > 10
print(b,'>',10,'=', result)

x = 10
y = 15

result = x is y
print("Value of x is",x,"id =", hex(id(x)))
print("Value of y is",y,"id =", hex(id(y)))
print(result)
result = x is not y
print(result)
