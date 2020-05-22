import awswrangler as wr

df = wr.athena.read_sql_query("SELECT * FROM emp_salary", database="test_data_wrangler")
print(df)

