def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a , b= b, a + b

num= int(input("No of fibonacci numbers need to be generated: "))

fibo = fibonacci()
for _ in range(num):
    print(next(fibo), end=" ")

print("\n")