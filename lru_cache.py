from collections import OrderedDict
from functools import wraps
import time 

def lru_cache(maximum=None):
    def decorator(func):
        cache = OrderedDict()
        @wraps(func)
        def decorated(*arg, **kwargs):
            key = (arg, tuple(sorted(kwargs.items())))
            if key in cache:
                val = cache[key]
                del cache[key]
            else:
                val = func(*arg, **kwargs)
            cache[key] = val
            if maximum and len(cache) > maximum:
                cache.popitem(last=False)
            return val
        return decorated
    return decorator 