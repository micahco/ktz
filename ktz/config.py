#!/usr/bin/python
import os
from configparser import RawConfigParser
from shutil import copyfile
from datetime import datetime

class Config():
    _PATH = 'config.ini'
    _TEMPLATE_PATH = 'config.template.ini'
    _path: str
    _rcp: RawConfigParser
    store: dict

    def __init__(self):
        self._path = os.path.join(os.getcwd(), self._PATH)
        self._rcp = RawConfigParser()
        
    def read(self) -> None:
        if not os.path.isfile(self._path):
            self.create()
        self._rcp.read(self._path)
        self.store = self._rcp['CONFIG'] # type: ignore

    def create(self) -> None:
        template_path = os.path.join(os.path.dirname(__file__), self._TEMPLATE_PATH)
        copyfile(template_path, self._path)
        self._rcp.read(self._path)
        print('\nCreating new configuration file')
        self._rcp.set('CONFIG', 'TemplatePath', input('TemplatePath = '))
        self._rcp.set('CONFIG', 'LiteraturePath', input('LiteraturePath = '))
        with open(self._path, 'w') as file:
            self._rcp.write(file)
        print('CREATED: ' + self._path)

    def validate(self) -> None:
        if not os.path.isfile(self.store['TemplatePath']):
            raise Exception('Invalid TemplatePath: ' + self.store['TemplatePath'])
        if not os.path.isdir(self.store['LiteraturePath']):
            raise Exception('Invalid LiteraturePath: ' + self.store['LiteraturePath'])
        if not self.store['DateFormat']:
            raise Exception('Invalid DateFormat: ')