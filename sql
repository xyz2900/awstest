CREATE EXTERNAL TABLE IF NOT EXISTS dat_forex (
  dtime timestamp,
  open  double,
  high  double,
  low   double,
  close  double,
  volume int 
)
PARTITIONED BY (year int, month int, day int)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
) LOCATION 's3://xyz2900/data/USD_JPY'
TBLPROPERTIES (
   'has_encrypted_data'='false',
   'skip.header.line.count'='1'
)

MSCK REPAIR TABLE dat_forex

/* add partition */
ALTER TABLE dat_forex ADD IF NOT EXISTS PARTITION (year=2020, month=01, day=02)

/* del partition */
ALTER TABLE dat_forex DROP IF EXISTS PARTITION (year=2020, month=01, day=01)
