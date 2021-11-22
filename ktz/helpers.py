#!/usr/bin/python
import os
import signal
import platform 

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
        if platform.system() == 'Windows':
                os.system('color')
        signal.signal(signal.SIGINT, _signal_handler)
        
def _signal_handler(signal, frame):
        abort()

def abort() -> None:
        print(f'{bcolors.WARNING}\n\nABORTED{bcolors.ENDC}')
        os._exit(0)

def error(e: Exception) -> None:
        e_name = e.__class__.__name__
        msg = f'{bcolors.FAIL}{e_name}{bcolors.ENDC}:'
        for arg in e.args:
                msg = msg + '\n' + arg
        _exit(msg)

def success(msg: str) -> None:
        print(f'\n{bcolors.OKGREEN}{msg}{bcolors.ENDC}')

def close(msg: str) -> None:
        _exit(f'\n{bcolors.OKGREEN}{msg}{bcolors.ENDC}')

def _exit(msg: str) -> None:
        print('\n' + msg)
        input(f'\n{bcolors.BOLD}Press any key to exit{bcolors.ENDC}')
        os._exit(0)