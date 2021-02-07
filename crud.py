import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

DATABASE = config['heroku_postgres']['HEROKU_DB_NAME']
USER = config['heroku_postgres']['HEROKU_DB_USER']
PASSWORD = config['heroku_postgres']['HEROKU_DB_PASSWORD']
HOST = config['heroku_postgres']['HEROKU_DB_HOST']
PORT = config['heroku_postgres'].getint('HEROKU_DB_PORT')


class ShowsDBCRUD:
    def __init__(self):
        self.con = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)

    def view_all_shows(self):
        print('view_all_shows crud.py')
        cur = self.con.cursor()
        cur.execute("""
            SELECT
                s.title,
                s.director,
                s.rating,
                s.release_year,
                s.country
            FROM shows s
            LIMIT 2;
            """)
        rows = cur.fetchall()
        return rows
