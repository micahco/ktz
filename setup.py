#!/usr/bin/python
import os
import platform 
from ktz.helpers import sig, success

sig()

ext: str
if platform.system() == 'Windows':
    ext = '.bat'
else:
    ext = '.sh'

default_path = os.path.expanduser("~/Desktop")
path = input(f'executable file location ({default_path}): ') or default_path
path = os.path.join(path, 'ktz' + ext)

data = 'python ' + os.path.join(os.path.dirname(__file__), 'ktz')

with open(path, 'w') as file:
    file.write(data)

success('CREATED: ' + path, True)