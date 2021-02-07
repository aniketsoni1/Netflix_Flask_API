from flask import Flask
from database import ShowsData

app = Flask(__name__)
database = ShowsData()


@app.route('/')
def index():
    return 'Welcome to the Netflix API!'


@app.route('/viewAllShows', methods=['GET'])
def view_all_shows():
    print('view_all_shows app.py')
    data = database.view_all_shows()
    return data
