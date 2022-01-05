from functools import wraps
import time


class CacheMgr:
    def __init__(self):
        self.cache_data = {}

    def cache(self, timeout=2):
        def ww(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                result = f(*args, **kwargs)
                return result

            return wrapper

        return ww
