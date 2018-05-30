import Module as mr
import Module
import os
import sys
from Module import wish_goodnight
from Module import *

mr.wish_guest("Alex")
if os.path.exists("Alex"):
    print("removing dir")
    os.removedirs("Alex")
print("creating dir")
os.mkdir("Alex")
print(sys.path)

wish_goodnight("Srikant")
wish_goodevening("Alec")


