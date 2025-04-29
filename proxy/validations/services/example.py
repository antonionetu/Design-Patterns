from time import sleep
from django.core.cache import cache


def example(request, user_id):
    sleep(5) # Process some data
    status = "ok"
    
    return {
        'id': user_id,
        'status': status
    }


def example_proxy(request, user_id):
    cache_key = f"example_proxy__{user_id}"
    cached_result = cache.get(cache_key)
    
    if cached_result:
        return cached_result

    result = example(request, user_id)
    cache.set(cache_key, result, timeout=10)
    return result
