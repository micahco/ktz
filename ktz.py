#!/usr/bin/python
import sys
import re
import os
from datetime import datetime
from shutil import copyfile
import easygui


# user vars
LITERATURE_PATH = '../../literature/'
TEMPLATE_PATH = '../../!templates/Clipping.md' # location to literature template
DATE_FORMAT = '%Y%m%d'
ENCODE_KINDLE = 'utf-8-sig' # native kindle 'My Clippings.txt' encode
ENCODE = 'utf-8' # unicode encode for new files


# create Books list
class Clipping:
    def __init__(self, title, loc, date, note):
        self.title = title
        self.loc = loc
        self.date = date
        self.note = note
    def __str__(self):
        return 'TITLE\n' + str(self.title) + '\nLOC\n' + str(self.loc) + '\nDATE\n' + str(self.date) + '\nNOTE\n' + str(self.note)
class Book:
    def __init__(self, authorFirst, authorLast, yearPub, c):
            self.clippings = [c]
            self.title = c.title
            self.authorFirst = authorFirst
            self.authorLast = authorLast
            self.yearPub = yearPub
            self.dir = LITERATURE_PATH + str(authorLast + yearPub)
    def add(self, clipping):
        self.clippings.append(clipping)
    def __str__(self):
        return 'TITLE\n' + str(self.title) + '\nAUTHOR_LAST\n' + str(self.authorLast) + '\nYEAR_PUB\n' + str(self.yearPub) + '\nDIR\n' + str(self.dir)
BOOKS = []


# parse text
with open(easygui.fileopenbox(), 'r', encoding=ENCODE_KINDLE, errors='ignore') as file:
    list = file.read().split('==========')
    del list[-1]
    titles = []
    for i in list:
        # parse text --> Clipping
        i = i.split('\n\n', 1) # split i --> [info , note]
        i[0] = i[0].strip()
        i[0] = i[0].split('\n') # split i[0] --> [title , data]
        data = i[0][1].split(' | ') # split data [page , loc , date]
        title = i[0][0].split('(')[0].strip()
        loc = data[1].split('Loc. ')[1].strip()
        date = data[2].split('Added on ')[1]
        date = datetime.strptime(date, '%A, %B %d, %Y, %I:%M %p') # format date
        date = date.strftime(DATE_FORMAT)
        note = i[1].strip().replace('\n', '\n\n')
        c = Clipping(title, loc, date, note)
        if not title in titles: # check if title already in books list
            print('\nTitle: ' + title)
            authorFirst = input("AuthorFirst: ")
            authorLast = input("AuthorLast: ")
            yearPub = input("YearPub: ")
            BOOKS.append(Book(authorFirst, authorLast, yearPub, c))
            titles.append(title)
        else:
            BOOKS[titles.index(title)].add(c)


# create fies for each book
for b in BOOKS:
    print(b.dir)
    if not os.path.isdir(b.dir): # check if dir already exists
        os.mkdir(b.dir)
    with open(TEMPLATE_PATH, 'r', encoding=ENCODE, errors='ignore') as templateFile:
        t = templateFile.read()
        for c in b.clippings:
            path = b.dir + '/' + b.authorLast + b.yearPub + '-' + c.loc + '.md'
            copy = 1
            while (os.path.isfile(path)): # check if file already exists
                if (copy == 10): exit() # overflow
                copy += 1
                path = path.replace('.md', '-' + str(copy) + '.md') # append filename with copy
            with open(path, 'w', encoding=ENCODE) as file:
                f = t.replace('{{date}}', c.date)
                f = f.replace('{{title}}', c.title)
                f = f.replace('{{author}}', b.authorFirst + ' ' + b.authorLast)
                f = f.replace('{{year}}', b.yearPub)
                f = f.replace('{{loc}}', c.loc)
                f = f.replace('{{note}}', c.note)
                file.write(f)

exit()
# create files
if not os.path.isdir(CLIPPING_PATH): # check if dir already exists
    os.mkdir(CLIPPING_PATH)
with open(TEMPLATE_PATH, 'r', encoding=ENCODE, errors='ignore') as templateFile:
    t = templateFile.read()
    for i in CLIPPINGS:
        path = CLIPPING_PATH + '/' + CLIPPING_DIR + '-' + i.loc +'.md'
        copy = 1
        while (os.path.isfile(path)): # check if file already exists
            if (copy == 10): exit()
            copy += 1
            path = CLIPPING_PATH + '/' + CLIPPING_DIR + '-' + i.loc + '-' + str(copy) +'.md'
        with open(path, 'w', encoding=ENCODE) as file:
            f = t.replace('{{date}}', i.date)
            f = f.replace('{{title}}', i.title)
            f = f.replace('{{author}}', CLIPPING_AUTHOR_FIRST + ' ' + CLIPPING_AUTHOR_LAST)
            f = f.replace('{{year}}', CLIPPING_YEAR)
            f = f.replace('{{loc}}', i.loc)
            f = f.replace('{{note}}', i.note)
            file.write(f)