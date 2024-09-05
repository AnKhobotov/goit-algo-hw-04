import sys

# def echo(*args):
#     for args in sys.argv:
#         print(args)

# print(sys.argv)
import random
from random import randrange
from colorama import init, AnsiToWin32, Fore, Back
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

a = 'hello'
for i in a:
    print(Fore.CYAN, i, file=stream)
# print(randrange(Fore.GREEN,Fore.BLUE,Fore.CYAN) for i in a  )

