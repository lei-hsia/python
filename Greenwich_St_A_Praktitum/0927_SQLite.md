### Execute order: 

**FROM & JOINs**: determine & filter rows/tables; JOIN的条件用ON <br> 
**WHERE**: more filters on rows <br>
**GROUP by**: combine those rows into group <br>
**HAVING**: filter groups<br>
**ORDER BY**: arrange the remaining rows/groups<br>
**LIMIT**: filters on the remaining rows/groups

### Join: 

1. left join(左联接) 返回包括左表中的所有记录和右表中联结字段相等的记录
2. right join(右联接) 返回包括右表中的所有记录和左表中联结字段相等的记录
3. inner join(等值连接) 只返回两个表中联结字段相等的行

CROSS JOIN: create a Cartesian product of rows from the joined tables;
Unlike the INNER JOIN and LEFT JOIN clauses, a CROSS JOIN doesn't have a join condition.

CROSS JOIN: combines every row from the 1st table ```table1``` w. every row from the 2nd
table ```table2``` to form the result set.

If the first table has ```N``` rows, the 2nd table has ```M``` rows, then the final 
result will have ```N*M``` rows.

### UNION:

````query_1 UNION [ALL] query_2 [ALL] query_3 ... ; ```

```UNION``` removes duplicate rows, where as ```UNION ALL``` does not remove; as a result, 
```UNION ALL``` runs faster than ```UNION```.

```
SELECT FirstName, LastName, 'Employee' AS Type
FROM employees
UNION
SELECT FirstName, LastName, 'Customer'
FROM customers
ORDER BY FirstName, LastName;
```

## too many info. The rest refers back to [SQLite tutorial](https://www.sqlitetutorial.net/)
