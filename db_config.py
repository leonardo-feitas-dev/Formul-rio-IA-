import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
            user="avnadmin",
            password="AVNS_Ls0n7PDs9MI1_RCNybT",
            host="pg-9280d25-leonardo-feitas-dev.g.aivencloud.com",
            port="19122",
            database="dbIA"
            )
    return conn
