import awswrangler
import numpy as np
import pandas as pd
from os import path

database = 'dev'

# AWS Data Wrangler の各処理はこのセッションを通じて行います
session = awswrangler.Session()


glue = session.boto3_session.client('glue')
#glue.create_database(DatabaseInput={'Name':database})

query = '''
    select * from test
'''

df = session.pandas.read_sql_redshift(
    sql=query
)


print("DONE")