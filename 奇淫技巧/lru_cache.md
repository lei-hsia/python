LC1223. Dice Roll Simulation

```
from functools import lru_cache
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9+7
        @lru_cache(None)
        def dp(i, j, k):
            # roll i times, rolled j, k times ahead
            if i == 0:
                return 1
            res = 0
            for d in range(6):
                if d != j:
                    res += dp(i-1, d, 1)
                elif k+1 <= rollMax[d]:
                    res += dp(i-1, d, k+1)
            res %= mod
            return res
        return dp(n, -1, 0) % mod
```
