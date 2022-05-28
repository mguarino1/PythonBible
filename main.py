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
    book = book[:1].upper() + book[1:]
    cur.execute("SELECT * FROM BibleVerses WHERE book_id=:book AND chapter=:chapter AND verse=:verse",
                {"book": book, "chapter": chapter, "verse": verse})
    row = cur.fetchone()
    verse = row[5] + ':' + str(row[0]) + ':' + str(row[1]) + '   ' + row[2]
    return verse


@app.get("/")
async def read_root():
    return "After URL enter 'book'/'chapter'/'verse' to find Bible verse.",
