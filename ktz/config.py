#!/usr/bin/python
from configparser import RawConfigParser
from os import path
from helpers import exit_

class Config:
    PATH = 'config.ini'
    template_path: str
    literature_path: str
    date_format: str

    def __init__(self):
        self._validate_file
        config = RawConfigParser()
        config.read(self.PATH)
        self.template_path = config['PATHS']['TemplatePath']
        self.literature_path = config['PATHS']['LiteraturePath']
        self.date_format = config['TEMPLATE']['DateFormat']

    def validate(self) -> None:
        try:
            self._is_valid()
        except FileNotFoundError as err:
            raise Exception('FileNotFoundError (' + err.args[0] + '): ' + err.args[1])
        except NotADirectoryError as err:
            raise Exception('NotADirectoryError (' + err.args[0] + '): ' + err.args[1])

    def _validate_file(self) -> None:
        if not path.exists(self.PATH):
            exit_('FileNotFoundError (Missing Config File): ')

    def _is_valid(self) -> None:
        if not path.isfile(self.template_path):
            raise FileNotFoundError('TEMPLATE_PATH', self.template_path)
        if not path.isdir(self.literature_path):
            raise NotADirectoryError('LITERATURE_PATH', self.literature_path)