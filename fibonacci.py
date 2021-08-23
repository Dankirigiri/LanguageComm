def fibonacci(limit):
    l = limit
    x = 0
    y = 1
    for i in range(l):
        z = x+y
        x = y
        y = z
        result = x