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

    def search_shows_by_title(self, search_phrase):
        print('search_shows_by_title crud.py')
        cur = self.con.cursor()
        cur.execute(f"""
            SELECT
                *
            FROM shows s
            WHERE s.title LIKE '%{search_phrase}%';
            """)
        rows = cur.fetchall()
        print(rows)
        return rows

    def filter_shows_by_country(self, country, limit, offset):
        print('filter by country crud.py')
        cur = self.con.cursor()
        cur.execute(f"""
            SELECT
                *
            FROM shows s
            WHERE s.country LIKE '%{country}%'
            LIMIT {limit}
            OFFSET {offset};
            """)
        rows = cur.fetchall()
        print(rows)
        return rows

    def filter_shows_by_rating(self, rating, limit, offset):
        print('filter by rating crud.py')
        cur = self.con.cursor()
        cur.execute(f"""
            SELECT
                *
            FROM shows s
            WHERE s.rating = '{rating}'
            LIMIT {limit}
            OFFSET {offset};
            """)
        rows = cur.fetchall()
        print(rows)
        return rows

    def filter_shows_by_release_year(self, release_year, limit, offset):
        print('filter by country crud.py')
        cur = self.con.cursor()
        cur.execute(f"""
            SELECT
                *
            FROM shows s
            WHERE s.release_year = {release_year}
            LIMIT {limit}
            OFFSET {offset};
            """)
        rows = cur.fetchall()
        print(rows)
        return rows

    def update_show_type(self, show_type, show_id):
        print('update_show_type crud.py')
        cur = self.con.cursor()
        cur.execute(f"""
            UPDATE shows
            SET type = '{show_type}'
            WHERE show_id = {show_id};
            """)
        self.con.commit()

    def delete_show_by_id(self, show_id):
        print('delete_show_by_id crud.py')
        cur = self.con.cursor()
        cur.execute(f"""
            DELETE FROM shows
            WHERE show_id = {show_id};
            """)
        self.con.commit()


    def insert_show(self, show_id, type, title, director, cast, country,
                    date_added, release_year, rating, duration, listed_in, description):
        print('insert_show crud.py')
        cur = self.con.cursor()
        cur.execute(f"""
            INSERT INTO shows (show_id, type, title, director, "cast", country,
             date_added, release_year, rating, duration, listed_in, description)
            VALUES ('{show_id}', '{type}', '{title}', '{director}', '{cast}', '{country}',
             '{date_added}', {release_year}, '{rating}', '{duration}', '{listed_in}', '{description}');
            """)
        self.con.commit()
