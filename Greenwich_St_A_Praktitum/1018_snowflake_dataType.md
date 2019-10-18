1. NUMERIC: ```NUMBER(Precision, Scale)```;
  1. Precision: total number of digits allowed;
  2. Scale: number of digits allowed to the right of decimal point;

for more Snowflake data types info: [click here](https://www.google.com/search?rlz=1C5CHFA_enGB721GB722&sxsrf=ACYBGNTpXZ85h7hr8u9tIfPEDoXJd964fQ%3A1571422159206&ei=z_-pXaiiDIizgge4laOoAg&q=snowflake+data+types&oq=snowflake+data+&gs_l=psy-ab.3.1.35i39j0l9.85030.91052..91964...2.4..1.215.1343.15j1j1......0....1..gws-wiz.......0i71j0i67j0i131i67j0i10i67j0i131j35i305i39j0i10j0i20i263.lMzAaGQRJPo)

2. DATE

Snowflake supports a single DATE data type for storing dates (with no time elements). DATE accepts dates in the most common forms (YYYY-MM-DD, DD-MON-YYYY, etc.). In addition, all accepted timestamps are valid inputs for dates.

--- 

Q: What if there are commas inside data cell ?

A: Create ```file format``` with option: ```FIELD_OPTIONALLY_ENCLOSED_BY = '<character>'```. Include this file format when ```COPY```.

---

#### ```COPY``` operation options: 
```
COPY INTO { internalStage | externalStage | externalLocation }
     FROM { [<namespace>.]<table_name> | ( <query> ) }
[ FILE_FORMAT = ( { FORMAT_NAME = '[<namespace>.]<file_format_name>' |
                    TYPE = { CSV | JSON | PARQUET } [ formatTypeOptions ] } ) ]
[ copyOptions ]
[ HEADER ]
```

### Create file format
```
CREATE [ OR REPLACE ] FILE FORMAT [ IF NOT EXISTS ] <name>
                      TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } [ formatTypeOptions ]
                      [ COMMENT = '<string_literal>' ]
```

Where file format option can be:
```
formatTypeOptions ::=
-- If FILE_FORMAT = ( TYPE = CSV ... )
     COMPRESSION = AUTO | GZIP | BZ2 | BROTLI | ZSTD | DEFLATE | RAW_DEFLATE | NONE
     RECORD_DELIMITER = '<character>' | NONE
     FIELD_DELIMITER = '<character>' | NONE
     FILE_EXTENSION = '<string>'
     ESCAPE = '<character>' | NONE
     ESCAPE_UNENCLOSED_FIELD = '<character>' | NONE
     DATE_FORMAT = '<string>' | AUTO
     TIME_FORMAT = '<string>' | AUTO
     TIMESTAMP_FORMAT = '<string>' | AUTO
     BINARY_FORMAT = HEX | BASE64 | UTF8
     FIELD_OPTIONALLY_ENCLOSED_BY = '<character>' | NONE
     NULL_IF = ( '<string1>' [ , '<string2>' , ... ] )
     EMPTY_FIELD_AS_NULL = TRUE | FALSE
-- If FILE_FORMAT = ( TYPE = JSON ... )
     COMPRESSION = AUTO | GZIP | BZ2 | DEFLATE | RAW_DEFLATE | NONE
     FILE_EXTENSION = '<string>'
-- If FILE_FORMAT = ( TYPE = PARQUET ... )
     COMPRESSION = AUTO | SNAPPY | NONE
     SNAPPY_COMPRESSION = TRUE | FALSE
```
