#!/usr/bin/python
import os
import platform 
from ktz.helpers import sig, success

sig()
if not platform.system() == 'Windows':
    raise NotImplementedError('Batch file generation only supported on Windows')
default_path = os.path.expanduser("~/Desktop").replace('/', '\\')
path = input(f'Batch file location ({default_path}): ') or default_path
path = os.path.join(path, 'ktz.bat').replace('/', '\\')
data = 'python ' + os.path.join(os.path.dirname(__file__), 'ktz')
with open(path, 'w') as file:
    file.write(data)
success('CREATED: ' + path)