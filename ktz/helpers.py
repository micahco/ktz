#!/usr/bin/python
import os
import signal

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def sig():
        os.system('color')
        signal.signal(signal.SIGINT, _signal_handler)

def error(title: str, e: Exception) -> None:
        e_name = e.__class__.__name__
        _exit(f'{bcolors.FAIL}{title}:{bcolors.ENDC}\n{e_name}: {e.args[0]}\n')

def success(msg: str, exit_: bool) -> None:
        msg = f'{bcolors.OKGREEN}{msg}{bcolors.ENDC}'
        if exit_:
                _exit(msg)
        else:
                print('\n' + msg)

def _exit(msg: str) -> None:
        print('\n' + msg)
        input(f'\n{bcolors.BOLD}Press any key to exit{bcolors.ENDC}')
        os._exit(0)

def _signal_handler(signal, frame):
        _exit('ABORTED')