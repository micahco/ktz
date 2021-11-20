#!/usr/bin/python
import os
from datetime import datetime
import easygui # type: ignore
from typing import Dict
from config import Config
from models import Book, Note


class App:
    _config: Config
    books: Dict[str, Book]

    def __init__(self, config: Config):
        self.config = config
        self.books = {}

    # open and parse `My Clippings.txt`
    def parse(self) -> None:
        try:
            with open(easygui.fileopenbox(), 'r', encoding='utf-8-sig', errors='ignore') as file:
                clippings: list[str] = file.read().split('==========')
        except:
            raise Exception
        for clipping in clippings:
            if not self._is_valid_clipping(clipping): continue
            clipping_data = clipping.split('\n\n', 1) # [info , text]
            info = clipping_data[0].strip().split('\n') # [title , data]
            title = info[0].split('(')[0].strip()
            data = info[1].split(' | ') # [page , loc , raw_date]
            loc = data[1].split('Loc. ')[1].split('-')[0].strip()
            raw_date = data[2].split('Added on ')[1]
            date = datetime.strptime(raw_date, '%A, %B %d, %Y, %I:%M %p').strftime(self.config.date_format)
            text = clipping_data[1].strip().replace('\n', '\n\n') # seperate note from highlighted text
            note = Note(loc, date, text)
            if not title in self.books:
                print('TITLE: ' + title)
                author_first = input("AUTHOR FIRST: ")
                author_last = input("AUTHOR LAST: ")
                year_published = input("YEAR PUB: ")
                self.books[title] = Book(title, author_first, author_last, year_published, note)
                print()
            else:
                self.books[title].add(note)

    # create note file for each note in each book
    def write(self) -> None:
        with open(self.config.template_path, 'r', encoding='utf-8') as template_file:
            template_data = template_file.read()
        for book in self.books.values():
            dir_ = book.get_dir(self.config.literature_path)
            if not os.path.isdir(dir_):
                os.mkdir(dir_)
            for note in book.notes:
                path = self._check_path(dir_ + '/' + book.author_last + book.year_published + '-' + note.loc + '.md')
                # replace template_data with new data
                data = template_data.replace('{{date}}', note.date)
                data = data.replace('{{title}}', book.title)
                data = data.replace('{{author}}', book.get_author())
                data = data.replace('{{year}}', book.year_published)
                data = data.replace('{{loc}}', note.loc)
                data = data.replace('{{text}}', note.text)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(data)

    def exit_(self, msg: str) -> None:
        print(msg)
        input('Press any key to exit')
        os._exit(0)

    # validate clipping item
    def _is_valid_clipping(self, clipping: str) -> bool:
        return ' | Added on ' in clipping

    # handle duplicate files path
    def _check_path(self, path: str) -> str:
        if os.path.isfile(path):
            path = path.replace('.md', '-2.md')
            i = 2
            while (os.path.isfile(path)):
                i += 1
                if (i==100): break # overflow
                path = path[:-4] + str(i) + path[-3:]
        return path