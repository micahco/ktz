#!/usr/bin/python

import sys
import re
import os
from datetime import datetime
from shutil import copyfile
import easygui


# input gui
reqData = ['Author Last', 'Author First', 'Publish Year']
litData = easygui.multenterbox('Literature Data', 'Clippings.py', reqData)
for i, input in enumerate(litData):
    if not input:
        easygui.msgbox('REQUIRED: ' + reqData[i], 'ERROR')
        exit()


# user vars
CLIPPING_AUTHOR_LAST = litData[0]
CLIPPING_AUTHOR_FIRST = litData[1]
CLIPPING_YEAR = litData[2]
CLIPPING_DIR = str(CLIPPING_AUTHOR_LAST + CLIPPING_YEAR) # i.e. Williams1937
CLIPPING_PATH = '../../literature/' + CLIPPING_DIR # path to new literature folder
TEMPLATE_PATH = '../../!templates/Clipping.md' # location to literature template
DATE_FORMAT = '%Y%m%d'


# create highlights list
class Highlight:
    def __init__(self, title, loc, date, quote):
        self.title = title
        self.loc = loc
        self.date = date
        self.quote = quote
    def __str__(self):
        return 'TITLE\n' + str(self.title) + '\nLOC\n' + str(self.loc) + '\nDATE\n' + str(self.date) + '\nQUOTE\n' + str(self.quote)
HIGHLIGHTS = []


# parse text
with open(easygui.fileopenbox(), 'r') as file:
    list = file.read().split('==========')
    for i in list:
        i = i.split('\n\n') # split i --> [info , quote]
        i[0] = i[0].split('\n- ') # split info --> [title , data]
        data = i[0][1].replace('Note', 'Highlight').split('Highlight on Page ')[1].split(' | ') # split data --> [page , loc , date]
        title = i[0][0].split('(')[0] # remove author from title
        loc = data[1].split('Loc. ')[1].split('-')[0].strip() # remove prefix and trailing quote
        date = data[2].split('Added on ')[1] # remove prefix quote
        date = datetime.strptime(date, '%A, %B %d, %Y, %I:%M %p') # format date
        date = date.strftime(DATE_FORMAT)
        quote = i[1].strip() # remove trailing /n from quote
        HIGHLIGHTS.append(Highlight(title, loc, date, quote))


# create files
if not os.path.isdir(CLIPPING_PATH): # check if dir already exists
    os.mkdir(CLIPPING_PATH)
for i in HIGHLIGHTS:
    path = CLIPPING_PATH + '/' + CLIPPING_DIR + '-' + i.loc +'.md'
    if not (os.path.isfile(path)): # check if file already exists
        copyfile(TEMPLATE_PATH, path)
        with open(path, 'r') as file:
            f = file.read()
            f = f.replace('{{date}}', i.date)
            f = f.replace('{{title}}', i.title)
            f = f.replace('{{author}}', CLIPPING_AUTHOR_FIRST + ' ' + CLIPPING_AUTHOR_LAST)
            f = f.replace('{{year}}', CLIPPING_YEAR)
            f = f.replace('{{loc}}', i.loc)
            f = f.replace('{{quote}}', i.quote)
            with open(path, 'w') as file:
                file.write(f)