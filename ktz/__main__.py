#!/usr/bin/python
from config import Config
from app import App

config = Config()
app = App(config)
try:
    config.validate()
except Exception as err:
    app.exit_(err.args[0])
try:
    app.parse()
except:
    app.exit_('ABORTED')
finally:
    app.write()
    app.exit_('TRANSFER COMPLETE')