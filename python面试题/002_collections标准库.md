colelctions是python一个集合模块，提供了很多有用的集合类

collections[文档](https://docs.python.org/3/library/collections.html)

collections: Container datatypes:

1. namedtuple()
2. deque
3. ChainMap
4. Counter
5. OrderedDict
6. defaultdict
7. UserDict
8. UserList
9. UserString

其中，```namedtuple, deque, Counter, OrderedDict, defaultdict```都是high-performance container dt.

---
#### namedtuple: 

```tuple```:不变集合/元祖; ```collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)```

```namedtuple```是一个函数, 用来创建一个自定义的```tuple```对象, 并且规定了```tuple```元素的数目, 并用属性
而不是索引来引用```tuple```的某个元素.

```
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(1, 2)
>>> p.x
1
>>> p.y
2
```

#### deque; 
```list```按照index高效访问，插入和删除元素就很慢； ```list```是线性存储；

```deque```是linked list一种, 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈:

```
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
```

```deque```除了实现了```list```的```append()```和```pop()```之外, 还支持```appendleft()```
和```popleft()```, 就可以高效往头部添加或者删除elements;

#### defaultdict

使用```dict```时，如果引用的Key不存在，就会抛出```KeyError```。
如果希望key不存在时，返回一个默认值，就可以用```defaultdict```：

```
>>> from collections import defaultdict
>>> dd = defaultdict(lambda: 'N/A')
>>> dd['key1'] = 'abc'
>>> dd['key1'] # key1存在
'abc'
>>> dd['key2'] # key2不存在，返回默认值
'N/A'
```

#### OrderedDict

保持key的顺序; **按照entry插入的顺序排序**

相同的key的插入情况: If a new entry overwrites an existing entry, the original insertion 
position is left unchanged. Deleting an entry and reinserting it will move it to the end.
```
>>> from collections import OrderedDict
>>> d = dict([('a', 1), ('b', 2), ('c', 3)])
>>> d # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
>>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

>>> od = OrderedDict()
>>> od['z'] = 1
>>> od['y'] = 2
>>> od['x'] = 3
>>> od.keys() # 按照插入的Key的顺序返回
['z', 'y', 'x']
```

```OrderedDict```可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
```
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)
```

#### Counter
```
>>> from collections import Counter
>>> c = Counter()
>>> for ch in 'programming':
...     c[ch] = c[ch] + 1
...
>>> c
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
```

