def factorial(num):
    if num == 1:
        return num
    else:
        result = factorial(num - 1)
    return num * result

num = int(input())
if (num == 0):
    print(1)
else:
    print(factorial(num))


