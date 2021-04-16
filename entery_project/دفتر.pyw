import os
from subprocess import call
import sys

__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))


path0 = os.path.join(__location__, 'GUIS/MainPage.py')
call([sys.executable, path0])
