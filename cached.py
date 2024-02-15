from functools import wraps
import os
import time
from typing import Any

CACHING_ENABLED = bool(int(os.environ.get("CACHING_ENABLED", "0")))


class CacheMgr:

    def __init__(self):
        self.cache_data = {}

    def cached_deco(self, timeout=2):

        def deco(f):
            last_result_time: float | None = None
            last_result: Any = None

            @wraps(f)
            def wrapper(*args, **kwargs):
                nonlocal last_result, last_result_time
                hit = True
                if not CACHING_ENABLED:
                    hit = False
                elif last_result_time is None or last_result is None:
                    hit = False
                elif time.time() - last_result_time >= timeout:
                    hit = False
                if not hit:
                    # nonlocal last_result, last_result_time
                    last_result = result = f(*args, **kwargs)
                    last_result_time = time.time()
                    return result
                else:
                    return last_result

            return wrapper

        return deco
