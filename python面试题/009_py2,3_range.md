### xrange

Python2使用xrange创建一个迭代器对象，使用range创建一个list数组

Python3使用range创建迭代器对象，移除了xrange: 就只是创建迭代器对象了

至于python2中的```xrange()```和```range()```的区别: 参考[这里:py2: xrange vs range](https://www.geeksforgeeks.org/range-vs-xrange-python/)
其实也就是4个区别: 
1. return type: ```xrange()``` returns a generator; ```range()``` returns a list;
2. memory: ```range > xrange```; 
3. operations: ```range```返回值是list, 所以所有list能用的ops都可以用在range返回值上; ```xrange```返回生成器对象，所以不仅只是遍历，还是只遍历一次，所以跟list相关的操作都不能用在xrange上面;
4. speed: ```xrange > range```;

python3 中的```range([start], stop)```: 从start开始，到stop，但是不包含stop
