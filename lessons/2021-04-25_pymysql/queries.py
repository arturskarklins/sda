import pymysql

with pymysql.connect(
        host='localhost',
        user='cinemauser',
        password='cinema123!',
        database='cinematic',
        cursorclass=pymysql.cursors.DictCursor  # default is tuple
) as connection:
    with connection.cursor() as cursor:
        query = """
            SELECT * 
            FROM movies
            LEFT JOIN directors
            ON movies.rating = directors.rating;
            SELECT * FROM directors
            """
        cursor.execute(query)

        # review what exact query will be ran
        # cursor.mogrify(query)

        for entry in cursor.fetchall():  # fetchmany(n), fetchone()
            print(entry)

        # drops tables
        # cursor.execute('DROP TABLE movies')
        # cursor.execute('DROP TABLE directors')
