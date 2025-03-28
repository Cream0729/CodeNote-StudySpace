import start
print('\n',start.get_table(1, 3))

# or
from start import get_table
print('\n', get_table(1,5))

# -as 'name'
import CrearMod as cm
print('\n', cm.ac_Table(-3,3))

from CrearMod import get_table  #It will be use the new one
print('\n', get_table(1,3))

from CrearMod import *
# Can't use sayHello()


from EasyMethodLib import StrDemo
from EasyMethodLib.TestForDef import test
print('\n', test(lambda x, y: x * y / 2, 5, 3), '\n')

import EasyMethodLib.Guess