'''
You have the name of the moudule to be imported but its being held up
in a string.
You would like to invoke import command on the string
'''

mod_name = 'math'

import importlib

mod = importlib.import_module(mod_name)

print(mod.sqrt(100))

mod = importlib.import_module("urllib.request")

u = mod.urlopen("http://www.python.org")
print(u.read().decode("utf-8"))
