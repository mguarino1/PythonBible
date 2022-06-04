import sqlite3

con = sqlite3.connect('bible.db')
cur = con.cursor()

""" cur.execute('''CREATE TABLE BibleVerses 
                (chapter integer,
                verse integer,
                text text,
                translation_id text,
                book_id text,
                book_name text)''') """

con.commit()
con.close()
