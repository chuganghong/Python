#!/usr/bin/python
#Filename: if.py

number = 23
t = True

while t:
    guess = int(raw_input('Enter an integer : '))
    if guess == number:
        t = False
        print 'Congratulations, you guessed it.'
        print "(but you do not win any prizes!)"
    elif guess < number:
        print 'No,it is a litter highter than that' #Another block
        #You can do whatever you want in a block ...
    else:
        print 'No,it is a little lower than that'
        #you must have guess > number to reach that

print 'Done'
#This last statement is always executed,after the if statement is executed
