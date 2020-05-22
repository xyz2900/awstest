#!/usr/bin/env python
import pandas

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
#df = pandas.read_gbq(sql, dialect='standard')

# Run a Standard SQL query with the project set explicitly
project_id = 'fx01-274505'
df = pandas.read_gbq(sql, project_id=project_id, dialect='standard')
print(df)