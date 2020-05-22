#!/usr/bin/env python
# aws athena のデータをcsvにダウンロード
from os import path
import pandas as pd
import numpy as np
import awswrangler as wr
import boto3

if __name__ == '__main__':
   df = pd.DataFrame({"id": [1, 2], "value": ["foo", "boo"]})

   '''
   # Storing data on Data Lake
   res = wr.s3.to_parquet(
      df=df,
      path="s3://xyz2900/test03/",
      dataset=True,
      database="default",
      table="tbl_test03"
   )
   print(res)

   # Retrieving the data directly from Amazon S3
   df = wr.s3.read_parquet(res['paths'], dataset=True)
   print(df)
   '''

   session = boto3.Session(aws_access_key_id='', aws_secret_access_key='', region_name='ap-northeast-1')

   res = wr.catalog.table(database="default", table="tbl_test03", boto3_session=session)
   print(res)

   # Retrieving the data from Amazon Athena
   df = wr.athena.read_sql_query('SELECT * FROM "default"."tbl_test03"', database='default', boto3_session=session)
   print(df)




