#!/usr/bin/python
import os
import signal
import sys

def _signal_handler(signal, frame):
        exit_('ABORTED')

def sig():
        signal.signal(signal.SIGINT, _signal_handler)

def exit_(msg: str) -> None:
        print('\n' + msg)
        input('Press any key to exit')
        os._exit(0)