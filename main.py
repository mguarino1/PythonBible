from enum import Enum
import sqlite3
import string

from fastapi import FastAPI
app = FastAPI()

try:
    con = sqlite3.connect('bible.db', check_same_thread=False)
    cur = con.cursor()
    print("db connected")
except:
    print("db error")


@app.get("/{book}/{chapter}/{verse}")
def getVerse(book: str, chapter: int, verse: int):
    cur.execute("SELECT * FROM BibleVerses WHERE book_id=:book AND chapter=:chapter AND verse=:verse",
                {"book": book, "chapter": chapter, "verse": verse})
    row = cur.fetchone()
    if row:
        verseRow = row[5] + ':' + str(row[0]) + \
            ':' + str(row[1]) + '   ' + row[2]
        return verseRow
    else:
        return "Verse not found."
    # return 'hello'


@app.get("/{book}")
def getBook(book: str):
    cur.execute("SELECT * FROM BibleVerses WHERE book_id=:book",
                {"book": book})
    rows = cur.fetchall()
    rows = [r[5] + ':' + str(r[0]) + ':' + str(r[1]) +
            '   ' + r[2] for r in rows]
    return rows


@app.get("/")
async def read_root():
    return "After URL enter 'book'/'chapter'/'verse' to find verse.",
