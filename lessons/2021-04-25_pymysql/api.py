import pymysql

# https://flask.palletsprojects.com/en/1.1.x/
from flask import Flask, jsonify

# init Flask app
app = Flask(__name__)


# routes as endpoints
@app.route('/')
def home():
    return 'Hello World!'


@app.route('/moviesjson')
def movies_json():
    with pymysql.connect(
            host='localhost',
            user='cinemauser',
            password='cinema123!',
            database='cinematic',
            cursorclass=pymysql.cursors.DictCursor
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM movies')
            # create and return json
            return jsonify(cursor.fetchall())


@app.route('/movieshtml')
def movies_html():
    with pymysql.connect(
            host='localhost',
            user='cinemauser',
            password='cinema123!',
            database='cinematic',
            cursorclass=pymysql.cursors.DictCursor
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM movies')
            result = cursor.fetchall()

            movies = ''
            for movie in result:
                movies += f"""
                    <tr>
                        <td>{movie.get('movie_id')}</td>
                        <td>{movie.get('title')}</td>
                        <td>{movie.get('year')}</td>
                        <td>{movie.get('category')}</td>
                        <td>{movie.get('director_id')}</td>
                        <td>{movie.get('rating')}</td>
                    </tr>
                """

            return f"""
                <table border=1>
                    <tr>
                        <th>movie_id</th>
                        <th>title</th>
                        <th>year</th>
                        <th>category</th>
                        <th>director_id</th>
                        <th>rating</th>
                    </tr>
                    {movies}
                </table>
            """


@app.route('/html/<movie_id>')
def html_table(movie_id):
    if movie_id in (None, ''):
        return 'Supply movie id'

    with pymysql.connect(
            host='localhost',
            user='cinemauser',
            password='cinema123!',
            database='cinematic',
            cursorclass=pymysql.cursors.DictCursor
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM movies WHERE movie_id = %s', movie_id)
            content = cursor.fetchone()

            if content is None:
                return f'No movie found by id {movie_id}'

            return f"""
                <table border=1>
                    <tr>
                        <th>movie_id</th>
                        <th>title</th>
                        <th>year</th>
                        <th>category</th>
                        <th>director_id</th>
                        <th>rating</th>
                    </tr>
                    <tr>
                        <td>{content.get('movie_id')}</td>
                        <td>{content.get('title')}</td>
                        <td>{content.get('year')}</td>
                        <td>{content.get('category')}</td>
                        <td>{content.get('director_id')}</td>
                        <td>{content.get('rating')}</td>
                    </tr>
                </table>
            """


@app.route('/test/<test_id>')
def test(test_id):
    return test_id


# development environment setup
app.run(debug=True)
