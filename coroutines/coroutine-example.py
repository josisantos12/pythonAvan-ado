def func():
    print('function start')
    yield
    print('function end')

    try:
        y=func()
        print(type(y))
        next(y)
        next(y)
    except StopIteration as e:
        pass