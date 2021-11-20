#!/usr/bin/python
import os

def exit_(msg: str) -> None:
        print(msg)
        input('Press any key to exit')
        os._exit(0)