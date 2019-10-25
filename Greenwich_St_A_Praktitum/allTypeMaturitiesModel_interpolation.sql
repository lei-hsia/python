-- snowsql

use fakeprice;
select * from jpmprice limit 50;

-- create table with all columns but model
-- select day, value, field1, field2, instrument_type, instrument_maturity, hold_horizon, attribute from jpmprice;
-- CANNOT use cross product because it's going to mismatch original value && type,maturity, etc. discard above approach

-- jpmprice table copy; used to add 3 models: ADABoost, Lasso w. residuals, logistic base
create table jpm5model as
select * from jpmprice;

select * from jpm5model limit 10;
select count(*) from jpm5model;

create table add_model as 
select * from (values (0.95)) as q (add_model_coeff);

select * from add_model;


create table jpm_addition_3model as 
select day, jpmcopy.value * add_model.add_model_coeff as value, field1, field2, instrument_type, instrument_maturity,
model, hold_horizon, attribute from jpmcopy cross join add_model;

select * from jpm_addition_3model limit 100;

update jpm_addition_3model 
set model='ADABoost' where model = 'ensemble2018' and value < 1;

update jpm_addition_3model 
set model='Lasso w. residuals' where model = 'ensemble2018' and value > 1;

update jpm_addition_3model 
set model='logistic base model' where attribute = 'position';

select count(*) from jpm_addition_3model; 
select count(*) from jpm_addition_3model where model = 'ADABoost';  -- 9178
select count(*) from jpm_addition_3model where model = 'Lasso w. residuals'; -- 9370
select count(*) from jpm_addition_3model where model = 'logistic base model'; -- 10021

-- combine original treasury 2-model table with 3-model table;
INSERT INTO jpm5model--(Structure, Name, Active)
   SELECT * FROM jpm_addition_3model;
   --UNION
   -- SELECT * FROM jpm5model; 
   
select * from jpm5model limit 100;

select count(*) from jpm5model  where model = 'ensemble2018'; -- 14445
select count(*) from jpm5model  where model = 'passive'; -- 14124
select count(*) from jpm5model  where model = 'ADABoost'; -- 9178
select count(*) from jpm5model  where model = 'Lasso w. residuals'; -- 9370
select count(*) from jpm5model  where model = 'logistic base model'; -- 10021
-- concludes creating table with 5 models, of type "treasury"

-- create IRS table based on above table
create table IRS as 
select * from jpm5model;

select * from IRS limit 5;

update IRS set instrument_type='IRS' where instrument_type='treasury';

create table irs_coeff as 
select * from (values (1.1)) as q (irs_coeff);

create table irs5model as 
select day, IRS.value * i.irs_coeff as value, field1, field2, instrument_type, instrument_maturity,
model, hold_horizon, attribute from IRS cross join irs_coeff i;

-- select count(*) from irs5model;

create table jpm_irs_5model as
SELECT * FROM jpm5model
   UNION
   SELECT * FROM irs5model; 
   
select count(*) from jpm_irs_5model; -- 114222, because jpm5model, irs5model both have 57138 rows

-- treasury and IRS type, 5 futures below
-- I did this without too much thinking: i.e. VALUES might have duplicates; 
-- I just replaced type, maturity with 5 futures names and NULL respectively.

-- ZT
create table ZT_temp as select * from jpm5model;
update zt_temp set instrument_type = 'ZT';
update zt_temp set instrument_maturity = NULL;
select * from zt_temp limit 5;

create table zt_coeff as 
select * from (values (0.88)) as q (zt_coef);

create table ZT as 
select day, zt_temp.value * zt_coeff.zt_coef as value, field1, field2, instrument_type, instrument_maturity,
model, hold_horizon, attribute from zt_temp cross join zt_coeff;

select * from zt limit 5;

-- ZN
create table ZN_temp as select * from jpm5model;
update zn_temp set instrument_type = 'ZN';
update zn_temp set instrument_maturity = NULL;
select * from zn_temp limit 5;

create table zn_coeff as 
select * from (values (0.92)) as q (zn_coef);

create table ZN as 
select day, zn_temp.value * zn_coeff.zn_coef as value, field1, field2, instrument_type, instrument_maturity,
model, hold_horizon, attribute from zn_temp cross join zn_coeff;

select * from zn limit 5;

-- ZB
create table ZB_temp as select * from jpm5model;
update zb_temp set instrument_type = 'ZB';
update zb_temp set instrument_maturity = NULL;
select * from zb_temp limit 5;

create table zb_coeff as 
select * from (values (0.85)) as q (zb_coef);

create table ZB as 
select day, zb_temp.value * zb_coeff.zb_coef as value, field1, field2, instrument_type, instrument_maturity,
model, hold_horizon, attribute from zb_temp cross join zb_coeff;

select * from zb limit 5;

-- FV
create table fv_temp as select * from jpm5model;
update fv_temp set instrument_type = 'fv';
update fv_temp set instrument_maturity = NULL;
select * from fv_temp limit 5;

create table fv_coeff as 
select * from (values (1.05)) as q (fv_coef);

create table fv as 
select day, fv_temp.value * fv_coeff.fv_coef as value, field1, field2, instrument_type, instrument_maturity,
model, hold_horizon, attribute from fv_temp cross join fv_coeff;

select * from fv limit 5;

-- UB
create table UB_temp as select * from jpm5model;
update UB_temp set instrument_type = 'UB';
update UB_temp set instrument_maturity = NULL;
select * from UB_temp limit 5;

create table UB_coeff as 
select * from (values (1.15)) as q (UB_coef);

create table UB as 
select day, UB_temp.value * UB_coeff.UB_coef as value, field1, field2, instrument_type, instrument_maturity,
model, hold_horizon, attribute from UB_temp cross join UB_coeff;

select * from UB limit 5;

-- done with all 13 types, with their respective maturities and models, without mismatching original data
create table all_original as
   SELECT * FROM jpm5model
   UNION
   SELECT * FROM irs5model
   UNION
   SELECT * FROM ZT
   UNION
   SELECT * FROM ZN
   UNION
   SELECT * FROM ZB
   UNION
   SELECT * FROM FV
   UNION
   SELECT * FROM UB;
   
select count(*) from all_original; -- rows: 365492


-- Achtung: interpolate
-- interpolation can only work on value with the same type, except for the day; i.e. 

-- interpolation is by day, with the same field1, field2, type, maturity, model, horizon and attribute.
-- everything to be the same, then interpolation can be carried out between two points ranging from a 
-- previous day to a second one. 
-- 
-- but, it is desired that the value for previous day be integrated into the value for current row, because the only
-- time the previous day value is right above, is when this value is ordered by day. When it is not, then you cannot 
-- say: using the value of the above row. 
-- 
-- How to incorporate the previous value into current row? : 
-- Order by every other field so that entries with the same
-- property are ordered by date. Using a window function lag... to incorporate previous price into current row, so that
-- every rows are atomic. Achtung that the first row would have a null. 
-- Cross join values from a sequence to form the new table w. added previous values, i.e. prior_value.
-- for each value and prior_value in the same row:
-- 
-- prior_value + (value - prior_value) / 24 * t.i new_value : gives the number of points desired on the line
-- between point A. value, and point B. prior_value. 
-- 
-- The only thing left: these values are on a strict straight line. Add some randomness to it.
-- 

create table hours as select seq4() i from table(generator(rowcount => 24));

select v.*, t.i, prior_value + (value - prior_value) / 24 * t.i new_value
from
    (select v.*, lag(value) over (partition by instrument_type, instrument_maturity, model, attribute order by day) as prior_value
    from 
        all_original v) v
    cross join hours t 
where prior_value is not null
order by instrument_type, instrument_maturity, model, attribute, day, t.i limit 50; 



   