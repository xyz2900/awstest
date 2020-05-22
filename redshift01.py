from awswrangler import Session, Redshift
import awswrangler as wr

con = Redshift.generate_connection(
        database="dev",
        host='redshift-cluster-1.cajhj66uu5bu.ap-northeast-1.redshift.amazonaws.com',
        port='5439',
        user="awsuser",
        password='Kaki.Kaki#8086'
    )

df = wr.pandas.read_sql_redshift(
    sql="SELECT * FROM test",
    iam_role="AWSServiceRoleForRedshift",
    connection=con)

    #temp_s3_path="s3://809392324773-titanic/titanic")

print(df)