# top-level scripts. I don't use that yet but could be useful.
# I'm guess you'd do that if you wanted stuff to be run with setup() calls in setup.py for example,
# perhaps things like configuring other programs/environment details upon install etc.
from pysetuptools.my_module import count_matrix

print(f"AND THE matrix count is: {count_matrix()}")
