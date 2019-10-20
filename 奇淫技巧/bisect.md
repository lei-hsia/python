1235. Maximum Profit in Job Scheduling

```
def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
```

#### 用法: 
1. bisect.bisect_left(a, x, lo=0, hi=len(a)), 或者(等价于2):
2. bisect.bisect(a, x, lo=0, hi=len(a)) 

不过最上面的例子， lee215是: 

bisect一个list of list based on the first element of the desired list; 因为只是desired list中的第一个元素, 所以写成了```[s + 1]```, 连逗号和后面的部分都没有写;

更多这种bisect二维的东西: 
```
list_of_tuples = [(3, 1), (2, 2), (5, 6)]

from bisect import bisect
bisect(list_of_tuples, (3, ))  # python 3.7
```

