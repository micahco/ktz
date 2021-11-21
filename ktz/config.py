#!/usr/bin/python
import os
from configparser import RawConfigParser
from shutil import copyfile
from helpers import success

class Config():
    _PATH = 'config.ini'
    _TEMPLATEpath = 'config.template.ini'
    _rcp: RawConfigParser
    path: str
    store: dict

    def __init__(self):
        self._rcp = RawConfigParser(comment_prefixes='/', allow_no_value=True)
        self._rcp.optionxform = str
        self.path = os.path.join(os.getcwd(), self._PATH)
        
    def read(self) -> None:
        if not os.path.isfile(self.path):
            self.create()
        self._rcp.read(self.path)
        self.store = self._rcp['CONFIG'] # type: ignore

    def create(self) -> None:
        templatepath = os.path.join(os.path.dirname(__file__), self._TEMPLATEpath)
        copyfile(templatepath, self.path)
        self._rcp.read(self.path)
        print('\nCreating new configuration file')
        self._rcp.set('CONFIG', 'TemplatePath', input('TemplatePath = '))
        self._rcp.set('CONFIG', 'LiteraturePath', input('LiteraturePath = '))
        with open(self.path, 'w') as file:
            self._rcp.write(file)
        success('CREATED: ' + self.path, False)
        

    def validate(self) -> None:
        if not os.path.isfile(self.store['TemplatePath']):
            raise FileNotFoundError('TemplatePath = ' + self.store['TemplatePath'])

        if not os.path.isdir(self.store['LiteraturePath']):
            raise NotADirectoryError('LiteraturePath = ' + self.store['LiteraturePath'])

        if not self.store['DateFormat']:
            raise ValueError('Missing DateFormat')