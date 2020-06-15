'''
Your package includes a data file that your code needs to read.
You need to do this in the most portable way possible.

modulesnpackages
|-- __init__.py
|-- check_data.py   <------------------- Reader
|-- importwithname.py
`-- spam
    |-- __init__.py
    |-- __pycache__
    |   `-- __init__.cpython-37.pyc
    `-- data.dat   <--------------------- Data file

In this case my .dat file is located in `spam`  package and thats the first argument
to get_data(package, resource)

If the .dat file was located in the same package, we could have used
get_data(__package__, resource)

One thing to note that, whatever is read from the get_data(), is a byte string.
'''


import pkgutil

data = pkgutil.get_data("spam", "data.dat")
print(data)