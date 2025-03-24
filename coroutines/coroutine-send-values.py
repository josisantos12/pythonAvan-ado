def my_coroutine():
    x = yield
    print(x)
    print('function part 1')

    a = yield
    print(a)
    print('function part 2')

try:
    y = my_coroutine()
    next(y)  # Start the coroutine
    y.send(5)
    y.send(6)
except StopIteration as e:
    pass