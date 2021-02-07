import data as data

from crud import ShowsDBCRUD
from flask import jsonify


class ShowsData:
    def __init__(self):
        self.db = ShowsDBCRUD()

    def view_all_shows(self):
        print('view_all_shows database.py')
        data = self.db.view_all_shows()
        data = jsonify(data)
        print('here', data)
        return data
