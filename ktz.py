#!/usr/bin/python
import sys
import re
import os
from datetime import datetime
from shutil import copyfile
import easygui


# input gui
reqData = ['Author Last', 'Author First', 'Publish Year']
litData = easygui.multenterbox('Literature Data', 'ktz', reqData)
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
ENCODE_KINDLE = 'utf-8-sig' # native kindle 'My Clippings.txt' encode
ENCODE = 'utf-8' # unicode encode for new files


# create Clippings list
class Clipping:
    def __init__(self, title, loc, date, note):
        self.title = title
        self.loc = loc
        self.date = date
        self.note = note
    def __str__(self):
        return 'TITLE\n' + str(self.title) + '\nLOC\n' + str(self.loc) + '\nDATE\n' + str(self.date) + '\nNOTE\n' + str(self.note)
CLIPPINGS = []


# parse text
with open(easygui.fileopenbox(), 'r', encoding=ENCODE_KINDLE, errors='ignore') as file:
    list = file.read().split('==========')
    del list[-1]
    for i in list:
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
        CLIPPINGS.append(Clipping(title, loc, date, note))


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