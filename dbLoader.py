import sqlite3
import json

asv = json.loads(open('asv.json').read())
#kjv = json.loads(open('kjv.json').read())
verseList = [tuple(x.values()) for x in asv]

con = sqlite3.connect('bible.db')
cur = con.cursor()

cur.executemany("INSERT INTO BibleVerses VALUES (?, ?, ?, ?, ?, ?)", verseList)

con.commit()
con.close()
