import os
import platform
import subprocess as sp

def clearscrn():
    if platform.system() == "'Linux'" or "'OSX'":
        sp.call('clear',shell=True)
    elif platform.system() == "'Windows'":
        sp.call('cls',shell=True)
