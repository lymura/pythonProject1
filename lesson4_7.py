def factorial(num):
    x = 1
    for i in range(1, num + 1):
        x *= i
        yield x

n = 12
for ind, el in enumerate(factorial(n)):
    print(f'#{ind + 1} {el}')