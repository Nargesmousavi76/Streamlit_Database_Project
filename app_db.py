import sqlite3 

DBNAME = "MoviesData.db"

def init_db():
    conn = sqlite3.connect(DBNAME)
    conn.close()

#init_db()
#################################################

def create_table():
    query = '''
        CREATE TABLE IF NOT EXISTS movies
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        year TEXT,
        country TEXT,
        imdb_rate REAL
        )
        '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

create_table()
#################################################

def insert_record(title,year,country,imdb_rate):
    query = '''
        INSERT INTO movies(title, year, country, imdb_rate)
        VALUES(?, ?, ?, ?)
            '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(title, year, country, imdb_rate))
    conn.commit()
    conn.close()

#insert_record("The Shawshank ","1994","USA",9.3)
#insert_record("The Godfather: Part II","1974","USA",9.0)
#insert_record("The Dark Knight","2008","USA,UK",9.0)
#insert_record("12 Angry Men","1957","USA",8.9)
#insert_record("Schindler's List","1993","USA",8.9)
#insert_record("Pulp Fiction","1994","USA",8.9)
#insert_record("he Lord of the Rings: The Return of the King","1966","USA,New Zealand",8.9)
#insert_record("The Good, the Bad and the Ugly","2020","Italy, Spain, West Germany,USA",8.9)
#insert_record("Fight Club","1999","USA, Germany",8.8)

#########################################################

def select_all_records():
    
    #query = 'SELECT title,year FROM movies'
    query = 'SELECT * FROM movies'

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    rows = cursor.execute(query).fetchall()
    conn.close()
    return rows

#print(select_all_records())
#########################################################

def select_record_by_id(id):
    query = 'SELECT *FROM movies WHERE id = ? '
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query,(id,)).fetchone()
    conn.close()
    return row

#print(select_record_by_id(2))
##############################################
def select_record_by_title(title):
    query = ' SELECT * FROM movies WHERE title=? '
    conn = sqlite3.Connection(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query,(title,)).fetchone()
    conn.close()
    return row

#print(select_record_by_title("Pulp Fiction"))

#################################################
def select_record_by_imdb_rate(imdb_rate):
    query = ' SELECT * FROM movies WHERE imdb_rate=? '
    conn = sqlite3.Connection(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query,(imdb_rate,)).fetchall()
    conn.close()
    return row

#print(select_record_by_imdb_rate(9.0))
    
#################################################

def delete_record_by_id(id):
    query = 'DELETE FROM movies WHERE id = ? '

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(id,))
    conn.commit()
    conn.close()
#delete_record_by_id(1)
#########################################
def delete_record_by_title(title):
    query = 'DELETE FROM movies WHERE title=? '

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(title,))
    conn.commit()
    conn.close()

#delete_record_by_title("Fight Club")
#################################################

def update_record_by_id(id,year, imdb_rate):
    query = '''
        UPDATE movies
        SET imdb_rate= ? , year = ?
        WHERE id = ?
            '''

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(imdb_rate, year, id))
    conn.commit()
    conn.close()

#update_record_by_id(2,"2026",4.6)
##############################################

def update_record_by_title(title,year,country,imdb_rate):
    query = '''
        UPDATE movies
        SET year=?, country=? , imdb_rate=?
        WHERE title=?
        '''

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(year,country,imdb_rate,title))
    conn.commit()
    conn.close()
#update_record_by_title("God Father","2000","UK",8.6)