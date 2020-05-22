#!/usr/bin/env python
# GAのデータを取得 ページビュー

from google2pandas import *

view_id = '169132398'

query = {
    'reportRequests': [{
        'viewId' : view_id,
        'dateRanges': [{
            'startDate' : '8daysAgo',
            'endDate'   : 'today'}],

        'dimensions' : [
            {'name' : 'ga:userAgeBracket'},
            {'name' : 'ga:userGender'},
            {'name' : 'ga:interestOtherCategory'},
        ],
        'metrics'   : [
            {'expression' : 'ga:percentNewSessions'}],
    }]
}

conn = GoogleAnalyticsQueryV4(secrets='./fx01-274505-5755e5b46f5b.json')
df = conn.execute_query(query)
print(df)



