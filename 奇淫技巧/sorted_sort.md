### sorted, 用于所有iterable

```sorted(iterable, [key=e.g. len], [reverse=e.g. True])```

| Parameter        |  Description | 
| ------------- |:-------------:| 
| iterable     | Required. The sequence to sort, list, dictionary, tuple etc. |
| key      | Optional. A Function to execute to decide the order. Default is None    | 
| reverse | Optional. A Boolean. False will sort ascending, True will sort descending. Default is False     | 

key: This argument expects a function to be passed to it, and that function will be used on each value in the list being sorted to determine the resulting order.
如果只是需要按照某个iterable的值来sort, 

##### sorted不改变original list:
```
>>> numbers = [6, 9, 3, 1]
>>> numbers_sorted = sorted(numbers)
>>> numbers_sorted
[1, 3, 6, 9]
>>> numbers
[6, 9, 3, 1]
```

### sort, 只能用于list
```list_name.sort(key=…, reverse=…) ```
改变original list; 

### 区别: 
1. ```sort``` can **only be used with lists**. 而```sorted()```可以用于所有的iterable.
2. ```.sort()``` returns None and modifies the values in place. 
