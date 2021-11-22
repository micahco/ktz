#!/usr/bin/python
from helpers import sig, error, close, success
from config import Config
from app import App

sig()
config = Config()
config.read()
try:
    config.validate()
    success('LOADED: ' + config.path)
except (FileNotFoundError, NotADirectoryError, ValueError) as e:
    error(f'ERROR ({config.path})', e)
except Exception as e:
    error('UNEXCPECTED ERROR', e)

app = App(config)
try:
    app.parse()
    app.write()
except FileNotFoundError as e:
    error('ERROR', e)
except Exception as e:
    error('UNEXPECTED ERROR', e)
close('TRANSFER COMPLETE')