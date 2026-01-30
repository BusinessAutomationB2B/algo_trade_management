import numpy
import scipy
from scipy import weave

#from scipy import weave

print('HELLO')

def py_print(input):
    print ("input:", input)
    
def c_print(input):
    code = """printf("Input: %i \\n", input);"""
    weave.inline(code,['input'])
    
py_print("hello from python")
c_print("hello from weave")