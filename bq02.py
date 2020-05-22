#!/usr/bin/env python
from google.cloud import bigquery

client = bigquery.Client()
sql = """
   SELECT
      *
   FROM
      `bigquery-public-data.ghcn_d.ghcnd_stations`
   WHERE
      latitude between 30 and 45 and
      longitude between 130 and 150
"""

# Run a Standard SQL query using the environment's default project
df = client.query(sql).to_dataframe()
print(df)

# Run a Standard SQL query with the project set explicitly
project_id = 'fx01-274505'
df = client.query(sql, project=project_id).to_dataframe()
print(df)