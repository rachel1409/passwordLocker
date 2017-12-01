import os
import platform
import subprocess as sp

def clearscrn():
    if platform.system == 'Windows' or 'OSX':
        sp.call('cls',shell=True)
    elif:
        sp.call('clear',shell=True)
