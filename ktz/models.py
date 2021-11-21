#!/usr/bin/python

class Note:
    loc: str
    date: str
    text: str

    def __init__(self, loc: str, date: str, text: str):
        self.loc = loc
        self.date = date
        self.text = text


class Book:
    title: str
    author_first: str
    author_last: str
    year_published: str
    notes: list[Note]

    def __init__(self, title: str, author_first: str, author_last: str, year_published: str, note: Note):
        self.title = title
        self.author_first = author_first
        self.author_last = author_last
        self.year_published = year_published
        self.notes = [note]

    def add(self, note: Note) -> None:
        self.notes.append(note)

    def get_author(self) -> str:
        return self.author_first + ' ' + self.author_last

    def get_dir(self, literature_path: str) -> str:
        return literature_path + '/' + self.author_last + self.year_published