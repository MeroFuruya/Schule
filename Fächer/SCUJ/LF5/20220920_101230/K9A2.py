# fabbonacci with for loop
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return b

for i in range(100):
    print(f(i))