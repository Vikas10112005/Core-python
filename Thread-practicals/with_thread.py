import threading
from threading import *

def hallo():
    for i in range(1,11):
        print("hallo:",i)

def hi():
    for i in range(1,11):
        print("hi:",i)

t1 = threading.Thread(target=hallo)
t2 = threading.Thread(target=hi)

t1.start()
t2.start()