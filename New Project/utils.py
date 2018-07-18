import os
import sys
from traceback import print_tb, extract_tb, format_list

def printError():
    error = sys.exc_info()
    typeError = error[0]#tipo do erro
    print('\n'+'Type: \n'+str(typeError)+'\n')
    value = error[1] # valor do erro
    print('Value: \n'+str(error[1])+'\n')
    tb=error[2]
    print('Traceback:')
    e_tb=extract_tb(tb)
    f_l=format_list(e_tb)#traceback em forma de lista para futuro usos
    print_tb(tb)
    return typeError, value, tb, f_l