import psycopg2
import pandas as pd

def get_connection():
    dsn = {
            "host":"redshift-cluster-1.cajhj66uu5bu.ap-northeast-1.redshift.amazonaws.com",      # ホスト名をここに記載
            "port":"5439",      # ポート番号をここに記載
            "database":"dev",  # DB名をここに記載
            "user":"awsuser",      # ユーザをここに記載
            "password":"Kaki.Kaki#8086",  # パスワードをここに記載
            }
    con = psycopg2.connect(**dsn)
    return con

def sql_test1(sql):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)