import awswrangler as wr

cols = ["id", "dt", "element", "value", "m_flag", "q_flag", "s_flag", "obs_time"]

path = f"s3://xyz2900/test03/"

df = wr.s3.read_csv(
    path="s3://noaa-ghcn-pds/csv/189",
    names=cols,
    parse_dates=["dt", "obs_time"])  # Read 10 files from the 1890 decade (~1GB)
print(df)

res = wr.s3.to_parquet(
    df=df,
    path=path,
    dataset=True,
    mode="overwrite",
    database="default",
    table="noaa"
)
print(res)

# paths: s3://xyz2900/test03/2e6f4b4d0392443aa873475095ae0b9f.snappy.parquet
df = wr.athena.read_sql_query("SELECT * FROM noaa", database="default")
print(df)


