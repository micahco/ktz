#!/usr/bin/python
import sys
import re
import os
from datetime import datetime
from shutil import copyfile
import easygui # type: ignore
# local
import config
from models import Book, Note


BOOKS: list[Book] = []
TITLES: list[str] = []


# parse `My Clippings.txt`
with open(easygui.fileopenbox(), 'r', encoding='utf-8-sig', errors='ignore') as file:
    clippings = file.read().split('==========')
    if not clippings[len(clippings)-1]:
        clippings.pop() # delete extraneous item at end of list
    for c in clippings:
        clippingData = c.split('\n\n', 1) # [info , text]
        info = clippingData[0].strip().split('\n') # [title , data]
        title = info[0].split('(')[0].strip()
        data = info[1].split(' | ') # [page , loc , date]
        loc = data[1].split('Loc. ')[1].split('-')[0].strip()
        dateRaw = data[2].split('Added on ')[1]
        date = datetime.strptime(dateRaw, '%A, %B %d, %Y, %I:%M %p').strftime(config.DATE_FORMAT)
        text = clippingData[1].strip().replace('\n', '\n\n')
        n = Note(loc, date, text)
        if not title in TITLES: # check if title already in books list
            print('\nTitle: ' + title)
            authorFirst = input("AuthorFirst: ")
            authorLast = input("AuthorLast: ")
            yearPub = input("YearPub: ")
            BOOKS.append(Book(title, authorFirst, authorLast, yearPub, n))
            TITLES.append(title)
        else:
            BOOKS[TITLES.index(title)].add(n)


# create fies for each book
for book in BOOKS:
    if not os.path.isdir(book.getDir()): # check if dir already exists
        os.mkdir(book.getDir())
    with open(config.TEMPLATE_PATH, 'r', encoding='utf-8') as templateFile:
        t = templateFile.read()
        for note in book.notes:
            path = book.getDir() + '/' + book.authorLast + book.yearPub + '-' + note.loc + '.md'
            copy = 1
            while (os.path.isfile(path)): # check if file already exists
                if (copy == 10): exit() # overflow
                copy += 1
                path = path.replace('.md', '-' + str(copy) + '.md') # append filename with copy
            with open(path, 'w', encoding='utf-8') as file:
                f = t.replace('{{date}}', note.date)
                f = f.replace('{{title}}', book.title)
                f = f.replace('{{author}}', book.authorFirst + ' ' + book.authorLast)
                f = f.replace('{{year}}', book.yearPub)
                f = f.replace('{{loc}}', note.loc)
                f = f.replace('{{text}}', note.text)
                file.write(f)


print('TRANSFER COMPLETE')