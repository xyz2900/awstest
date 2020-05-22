import pandas_redshift as pr

pr.connect_to_redshift(dbname = "dev",
                        host = 'redshift-cluster-1.cajhj66uu5bu.ap-northeast-1.redshift.amazonaws.com',
                        port = '5439',
                        user = 'awsuser',
                        password = 'Kaki.Kaki#8086')

df = pr.redshift_to_pandas('select * from test')

