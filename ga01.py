#!/usr/bin/env python
# GAのデータを取得　ページビュー
import os
import datetime as dt
import awswrangler as wr
from google2pandas import *

view_id = '169132398'

yesteday = dt.date.today() - dt.timedelta(days=1)

query = {
   'reportRequests': [{
   'viewId' : view_id,

   'dateRanges': [{
   'startDate' : '1daysAgo',
   'endDate'   : '1daysAgo'}],

   'dimensions' : [
      {'name' : 'ga:date'},
      {'name' : 'ga:pagePath'},
      {'name' : 'ga:browser'}],

   'metrics'   : [
            {'expression' : 'ga:pageviews'}],
    }]
}

jsonfile = os.path.dirname(__file__) + '/fx01-274505-5755e5b46f5b.json'
conn = GoogleAnalyticsQueryV4(secrets=jsonfile)
df = conn.execute_query(query)

path = f"s3://xyz2900/GA/year=%4d/month=%d/dt=%04d-%02d-%02d/%04d%02d%02d.csv" % (yesteday.year, yesteday.month, yesteday.year, yesteday.month, yesteday.day, yesteday.year, yesteday.month, yesteday.day)
res = wr.s3.to_csv(df, path, index=False, dataset=True, database="default", table='ga_pv')

'''
res = wr.s3.to_parquet(
    df=df,
    path=path,
    dataset=True,
    mode="overwrite",
    database="default",
    table="noaa"
)
'''
print(res)





