import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
            user="avnadmin",
            password="I67KnpDQtqo7Zw0kz6fXvJFZsm4fLCK1",
            host="dpg-cpkuddnsc6pc73f50vl0-a",
            port="5432",
            database="dbia"
            )
    return conn
