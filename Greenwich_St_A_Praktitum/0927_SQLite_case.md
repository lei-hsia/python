```
CASE case_expression
     WHEN when_expr_1 THEN result_1
     WHEN when_expr_2 THEN result_2
     ...
     [ ELSE result_else ]
END
```

e.g. 
```
SELECT customerid, 
       firstname,
       lastname,
       CASE country
            WHEN 'USA'
                THEN 'Domestic'
            ELSE 'Foreign'
       END CustomerGroup
FROM
    customers
ORDER BY
    Lastname,
    Firstname;
```

```
SELECT
    trackid,
    name,
    CASE
        WHEN milliseconds < 60000 THEN
            'short'
        WHEN milliseconds > 60000 AND milliseconds < 300000 THEN 'medium'
        ELSE 
            'long'
        END category
FROM
    tracks;
```
