### sorted: 

```sorted(iterable, [key=e.g. len], [reverse=e.g. True])```

| Parameter        |  Description | 
| ------------- |:-------------:| 
| iterable     | Required. The sequence to sort, list, dictionary, tuple etc. |
| key      | Optional. A Function to execute to decide the order. Default is None    | 
| reverse | Optional. A Boolean. False will sort ascending, True will sort descending. Default is False     | 

##### sorted不改变original list:
```
>>> numbers = [6, 9, 3, 1]
>>> numbers_sorted = sorted(numbers)
>>> numbers_sorted
[1, 3, 6, 9]
>>> numbers
[6, 9, 3, 1]
```

### sort:

### 区别: 
1. ```sort``` is a method of the list class and can **only be used with lists**. It is not a built-in with an iterable passed to it.

2. ```.sort()``` returns None and modifies the values in place. 
