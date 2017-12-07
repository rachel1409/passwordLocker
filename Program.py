import client
import server
import os
import time
import no_bytecode
from ClearScreen import *

if __name__ == '__main__':
    clearscrn()
    os.system('python -B server.py &')
    time.sleep(2)
    os.system('python -B client.py')
