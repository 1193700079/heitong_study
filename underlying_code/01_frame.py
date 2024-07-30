import inspect
from objprint import op


def f():
    frame = inspect.currentframe()
    print(frame.f_back.f_code.co_name)
    print(frame.f_back.f_locals)
    print(frame.f_back.f_code.co_filename)
    print(frame.f_back.f_lineno)

    op(frame, honor_existing=False, depth=1)


def g():
    a = 3
    b = 4
    f()


g()
