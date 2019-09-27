```
SELECT
    CustomerId,
    FirstName,
    LastName,
    Company
FROM
    Customers c
WHERE
    EXISTS (
        SELECT 
            1 
        FROM 
            Invoices
        WHERE 
            CustomerId = c.CustomerId
    )
ORDER BY
    FirstName,
    LastName; 
```

has the same effect as: 
```
SELECT
   CustomerId, 
   FirstName, 
   LastName, 
   Company
FROM
   Customers c
WHERE
   CustomerId IN (
      SELECT
         CustomerId
      FROM
         Invoices
   )
ORDER BY
   FirstName, 
   LastName;
```
Diff: 

1. Once the subquery returns the first row, the ```EXISTS``` operator stops searching because 
it can determine the result. On the other hand, the  ```IN``` operator must scan all rows
returned by the subquery to determine the result.

2. Generally speaking, ```EXISTS``` operator is faster than ```IN``` if the result set returned
by the subquery is large. By contrast, the ```IN``` operator is faster than the ```EXISTS```
operator if the result set returned by the subquery is small.

