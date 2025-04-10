from typing import Callable


def cache(func: Callable) -> Callable:

    def inner(*args) -> Callable:
        cache_date = {}
        if args in cache_date:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_date[args] = func(*args)
        return cache_date[args]
    return inner
