#!/usr/bin/python
import config

class Note:
    loc: str
    date: str
    text: str
    path: str

    def __init__(self, loc: str, date: str, text: str):
        self.loc = loc
        self.date = date
        self.text = text

    def __str__(self) -> str:
        return 'LOC: ' + self.loc + '\nDATE: ' + self.date + '\nTEXT: ' + self.text


class Book:
    title: str
    authorFirst: str
    authorLast: str
    yearPub: str
    notes: list[Note]

    def __init__(self, title: str, authorFirst: str, authorLast: str, yearPub: str, n: Note):
        self.authorFirst = authorFirst
        self.authorLast = authorLast
        self.title = title
        self.yearPub = yearPub
        self.notes = [n]

    def __str__(self) -> str:
        return 'len: ' + str(len(self.notes))

    def add(self, n: Note) -> None:
        self.notes.append(n)

    def getDir(self) -> str:
        return config.LITERATURE_PATH + '/' + self.authorLast + self.yearPub