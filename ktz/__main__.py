#!/usr/bin/python
from config import Config
from app import App
from helpers import sig, exit_

sig()
config = Config()
config.read()
try:
    config.validate()
except Exception as err:
    exit_('Config error:\n' + err.args[0])

app = App(config)
try:
    app.parse()
except FileNotFoundError as err:
    exit_('INVALID "MyClippings.txt" path: ' + err.args[0])
except Exception as err:
    exit_(err.args[0])
app.write()
exit_('TRANSFER COMPLETE')