#!/usr/bin/python
import sys
import re
import os
from datetime import datetime
import easygui # type: ignore
# typing
from typing import Dict, List
# local
import config
from models import Book, Note


# instantiate global vars
BOOKS: Dict[str, Book] = {}


# parse `My Clippings.txt`
with open(easygui.fileopenbox(), 'r', encoding='utf-8-sig', errors='ignore') as file:
    clippings = file.read().split('==========')
    for c in clippings:
        if not ' | Added on ' in c:
            continue
        clippingData = c.split('\n\n', 1) # [info , text]
        info = clippingData[0].strip().split('\n') # [title , data]
        title = info[0].split('(')[0].strip()
        data = info[1].split(' | ') # [page , loc , dateRaw]
        loc = data[1].split('Loc. ')[1].split('-')[0].strip()
        dateRaw = data[2].split('Added on ')[1]
        date = datetime.strptime(dateRaw, '%A, %B %d, %Y, %I:%M %p').strftime(config.DATE_FORMAT)
        text = clippingData[1].strip().replace('\n', '\n\n') # seperate note from highlighted text
        n = Note(loc, date, text)
        if not title in BOOKS: # check if title already in books list
            print('Title: ' + title)
            authorFirst = input("AuthorFirst: ")
            authorLast = input("AuthorLast: ")
            yearPub = input("YearPub: ")
            BOOKS[title] = Book(title, authorFirst, authorLast, yearPub, n)
            print()
        else:
            BOOKS[title].add(n)


# handle duplicate files path
def checkPath(path: str) -> str:
    if os.path.isfile(path):
        path = path.replace('.md', '-2.md')
        i = 2
        while (os.path.isfile(path)):
            i += 1
            if (i==10): break # overflow
            path = path[:-4] + str(i) + path[-3:]
    return path


# create note file for each note in each book
with open(config.TEMPLATE_PATH, 'r', encoding='utf-8') as templateFile:
    t = templateFile.read()
    for book in BOOKS.values():
        if not os.path.isdir(book.getDir()): # check if dir already exists
            os.mkdir(book.getDir())
        for note in book.notes:
            path = checkPath(book.getDir() + '/' + book.authorLast + book.yearPub + '-' + note.loc + '.md')
            with open(path, 'w', encoding='utf-8') as file:
                f = t.replace('{{date}}', note.date)
                f = f.replace('{{title}}', book.title)
                f = f.replace('{{author}}', book.authorFirst + ' ' + book.authorLast)
                f = f.replace('{{year}}', book.yearPub)
                f = f.replace('{{loc}}', note.loc)
                f = f.replace('{{text}}', note.text)
                file.write(f)


print('\nTRANSFER COMPLETE')
input("Press any key to exit")