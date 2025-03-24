def func():
    x = 5
    print('function part 1')
    yield x
    x += 1
    print('function part 2')
    yield x
    print('function part 3')

try:
    y = func()
    z = next(y)
    print(z)
    z = next(y)
    print(z)
    z = next(y)
    print(z)
except StopIteration as e:
    pass