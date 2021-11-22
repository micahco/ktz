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
    error(e)
except Exception as e:
    error(e)

app = App(config)
try:
    app.parse()
    app.write()
except Exception as e:
    error(e)
close('TRANSFER COMPLETE')