from pyathena import connect
import pandas as pd
aws_access_key_id = ''
aws_secret_access_key = ''

conn = connect(aws_access_key_id=aws_access_key_id,
                 aws_secret_access_key=aws_secret_access_key,
                 s3_staging_dir='s3://xyz2900/test03/',
                 region_name='ap-northeast-1')

df = pd.read_sql("SELECT * FROM noaa", conn)
print(df)