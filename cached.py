from functools import wraps
import time


class CacheMgr:
    def __init__(self):
        self.cache_data = {}

    def cache(self, timeout=2):
        def ww(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                if (f.__name__, args, tuple(kwargs.keys()), tuple(kwargs.values())) in self.cache_data.keys():
                    if self.cache_data[(f.__name__, args, tuple(kwargs.keys()), tuple(kwargs.values())
                                        )][0] - time.time() < timeout:
                        return self.cache_data[(f.__name__, args, tuple(kwargs.keys()), tuple(kwargs.values()))][1]
                result = f(*args, **kwargs)
                self.cache_data[(f.__name__, args, tuple(kwargs.keys()), tuple(kwargs.values()))] = (time.time(),
                                                               result)
                return result

            return wrapper

        return ww