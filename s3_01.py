import awswrangler as wr

df = wr.s3.read_parquet("s3://xyz2900/test03/2e6f4b4d0392443aa873475095ae0b9f.snappy.parquet")
print(df)

