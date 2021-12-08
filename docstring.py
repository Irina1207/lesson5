from functools import wraps
from typing import Optional


def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    return wrapper

def test(arg1, arg2):
    """
    Общее описание
    Пример кода

    :param arg1:  Описание параметра
    :param arg2:
    :return:
    """
    ...

@decorator
def test2(arg1, arg2):
    ...

print(f"Я вызываюсь при импорте и выполнение скрипта {__name__}")
if __name__ == '__main__':
    print(test.__name__)
    print(test.__doc__)

    help(test)