import awswrangler as wr

df = wr.s3.read_csv("s3://xyz2900/test03/h25_salary.csv")
print(df)

