from cache.cache import Cache


def cache(f):
    my_cache = Cache()

    def inner(*args):
        if my_cache.check(args):
            return my_cache.get(args)
        else:
            my_cache.set(args, f(*args))
            return my_cache.get(args)

    return inner


def type_check(checked_type):
    def decorator(f):
        def inner(*args):
            for el in args:
                if type(el) is not checked_type:
                    raise TypeError(
                        f"The argument must be of type {checked_type}, passed a {type(el)}."
                    )
            return f(*args)

        return inner

    return decorator


@cache
@type_check(int)
def int_sum(*args):
    return sum(args)