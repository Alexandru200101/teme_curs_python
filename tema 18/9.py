def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a  
        a, b = b, a + b  

n = 10
for termen in fibonacci(n):
    print(termen)
