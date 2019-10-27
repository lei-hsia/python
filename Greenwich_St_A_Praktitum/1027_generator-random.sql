select random(4711) from table(generator(rowcount => 5));

-- generator: generators ROWCOUNT rows values;
-- seq4(): index, starting from 0                                         
select seq4(), uniform(1, 10, random(12)) from table(generator(rowcount => 100)) v;
