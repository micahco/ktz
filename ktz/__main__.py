#!/usr/bin/python
from config import Config
from app import App
from helpers import exit_

config = Config()
app = App(config)

try:
    config.validate()
except Exception as err:
    exit_(err.args[0])

try:
    app.parse()
except:
    exit_('ABORTED')
finally:
    app.write()
    exit_('TRANSFER COMPLETE')