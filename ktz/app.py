#!/usr/bin/python
import os
from datetime import datetime
from typing import Dict
from helpers import bcolors
from config import Config
from models import Book, Note

class App:
    _config: dict
    books: Dict[str, Book]

    def __init__(self, config: Config):
        self._config = config.store
        self.books = {}

    # open and parse `My Clippings.txt`
    def parse(self) -> None:
        clippings_path = self._get_path()
        if not os.path.isfile(clippings_path):
            raise FileNotFoundError(clippings_path)
        with open(clippings_path, 'r', encoding='utf-8-sig', errors='ignore') as file:
            clippings: list[str] = file.read().split('==========')
        for clipping in clippings:
            if not self._is_valid_clipping(clipping): continue
            clipping_data = clipping.split('\n\n', 1) # [info , text]
            info = clipping_data[0].strip().split('\n') # [title , data]
            title = info[0].split('(')[0].strip()
            data = info[1].split(' | ') # [page , loc , raw_date]
            loc = data[1].split('Loc. ')[1].split('-')[0].strip()
            raw_date = data[2].split('Added on ')[1]
            date = datetime.strptime(raw_date, '%A, %B %d, %Y, %I:%M %p').strftime(self._config['DateFormat'])
            text = clipping_data[1].strip().replace('\n', '\n\n') # seperate note from highlighted text
            note = Note(loc, date, text)
            if not title in self.books:
                print(f'\n{bcolors.UNDERLINE}TITLE: {title}{bcolors.ENDC}')
                author_first = input("AuthorFirst: ")
                author_last = input("AuthorLast: ")
                year_published = input("YearPublished: ")
                self.books[title] = Book(title, author_first, author_last, year_published, note)
            else:
                self.books[title].add(note)

    # create note file for each note in each book
    def write(self) -> None:
        with open(self._config['TemplatePath'], 'r', encoding='utf-8') as template_file:
            template_data = template_file.read()
        for book in self.books.values():
            dir_ = book.get_dir(self._config['LiteraturePath'])
            if not os.path.isdir(dir_):
                os.mkdir(dir_)
            for note in book.notes:
                path = self._validate_note_path(dir_ + '/' + book.author_last + book.year_published + '-' + note.loc + '.md')
                # replace template_data with new data
                data = template_data.replace('{{date}}', note.date)
                data = data.replace('{{title}}', book.title)
                data = data.replace('{{author}}', book.get_author())
                data = data.replace('{{year}}', book.year_published)
                data = data.replace('{{loc}}', note.loc)
                data = data.replace('{{text}}', note.text)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(data)

    def _get_path(self) -> str:
        prompt = '\n"My Clippings.txt" path: '
        default = self._config['MyClippingsPath']
        if default:
            prompt += f'({default}) '
        return input(prompt) or default

    # validate clipping item
    def _is_valid_clipping(self, clipping: str) -> bool:
        return ' | Added on ' in clipping

    # handle duplicate note files
    def _validate_note_path(self, path: str) -> str:
        if os.path.isfile(path):
            path = path.replace('.md', '-2.md')
            i = 2
            while (os.path.isfile(path)):
                i += 1
                if (i==100): break # overflow
                path = path[:-4] + str(i) + path[-3:]
        return path