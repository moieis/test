import time

from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import pandas as pd

def start():
    s=input('dsfhsd',type=TEXT)
    put_text(s)
    popup('',s)
    data = pd.DataFrame({'hi':[23]})
    time.sleep(9)
    put_html(data)


start_server(start,port=0,debug=False,host='',cdn=True)
