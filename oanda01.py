#!/usr/bin/env python
# oandaから取得した分足データをS3にアップロード（HIVE形式)

import datetime as dt
import pandas as pd
import awswrangler as wr

def daterange(_start, _end):
   oneday = dt.timedelta(days=1)
   for n in range((_end - _start + oneday).days):
      yield _start + dt.timedelta(n)

def s3_upload(symbol, _date):
   csvfile = "/Users/Share/Projects/oanda/hist/USD_JPY/%04d%02d%02d.csv" % (_date.year, _date.month, _date.day)
   try:
      df = pd.read_csv(csvfile, dtype={'open':'double', 'high':'double', 'low':'double', 'close':'double'}, parse_dates=['dtime',], index_col=False)
      df['dtime'] = df['dtime'].dt.tz_localize(None) # tzを削除(athenaで読めない)

      path = "s3://xyz2900/data/USD_JPY/year=%04d/month=%02d/day=%02d/%04d%02d%02d.csv" % (_date.year, _date.month, _date.day, _date.year, _date.month, _date.day)
      res = wr.s3.to_csv(df, path, index=False)
      print(res)
   except Exception as e:
      print(e)

if __name__ == '__main__':
   symbol_list = ['USD_JPY', ]
   start_date = dt.date(2020, 1, 1)
   end_date   = dt.date(2020, 4, 22)

   # S3へアップロード
   for symbol in symbol_list:
      for _date in daterange(start_date, end_date):
         s3_upload(symbol, _date)

   # athenaのテーブルを作成
   sql = """
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
   """

   print("QUERY EXECUTE")
   query_exec_id = wr.athena.start_query_execution(sql=sql, database='default')
   print("WAITING")
   res = wr.athena.wait_query(query_execution_id=query_exec_id)
   print("DONE")


   # データの登録?
   sql = "MSCK REPAIR TABLE dat_forex"

   print("QUERY EXECUTE")
   query_exec_id = wr.athena.start_query_execution(sql=sql, database='default')
   print("WAITING")
   res = wr.athena.wait_query(query_execution_id=query_exec_id)
   print("DONE")

