lru_cache: [@lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)

### Decorator: ```@functools.**lru_cache**(maxsize=128, typed=False)```

Also: ```cache_info```, ```cache_clear```

In general, the LRU cache should only be used when you want to reuse previously computed values.

Examples of LRU cache w. static web content: 
```
@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'

>>> for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
...     pep = get_pep(n)
...     print(n, len(pep))

>>> get_pep.cache_info()
CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
```

Examples of efficient computing in DP:
```
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> [fib(n) for n in range(16)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

>>> fib.cache_info()
CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
```
To help measure the effectiveness of the cache and tune the maxsize parameter, the wrapped function is instrumented with a ```cache_info()``` function that returns a named tuple showing <i>hits, misses, maxsize and currsize</i>. In a multi-threaded environment, the hits and misses are approximate.
