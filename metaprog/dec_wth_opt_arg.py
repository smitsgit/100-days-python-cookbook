from functools import partial, wraps


def log(func=None, *, prefix=None):
    if func is None:
        return partial(log, prefix=prefix)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{prefix}: {func.__name__}")
        result = func(*args, **kwargs)
        return result

    return wrapper


@log(prefix="####")
def spam():
    print("Hello World")


if __name__ == '__main__':
    spam()

# spam = log(prefix='####')(spam)
