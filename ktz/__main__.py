#!/usr/bin/python
from helpers import sig, error, close, success
from config import Config
from app import App

sig()
try:
    config = Config()
    config.read()
    config.validate()
    success('LOADED: ' + config.path)
    app = App(config)
    app.parse()
    app.write()
except Exception as e:
    error(e)
close('TRANSFER COMPLETE')