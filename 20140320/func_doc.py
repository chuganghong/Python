# Filename:func_doc.py

def printMax(x,y):
    '''Prints the maxinum of two numbers.

The two values must be integers.'''

    x = int(x) # convert to integers,if possible
    y = int(y)

    if x > y:
        print x, 'is maxinum'
    else:
        print y, 'is maxinum'

printMax(3, 5)
print printMax.__doc__
