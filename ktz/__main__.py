#!/usr/bin/python
from helpers import sig, error, success
from config import Config
from app import App

sig()
config = Config()
config.read()
try:
    config.validate()
    success('LOADED: ' + config.path, False)
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
except RuntimeError as e:
    error('ABORTED', e)
except Exception as e:
    error('UNEXPECTED ERROR', e)
success('TRANSFER COMPLETE', True)