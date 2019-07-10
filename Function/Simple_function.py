def a():
    return b() + c()

def b():
    return 3

def c():
    return 7 * b()

print a()