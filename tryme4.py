def new_line(): # function that prints one line.

    print('.')

    
def three_lines(): # function that prints 3 lines.

    new_line()

    new_line()

    new_line()

    
def nine_lines(): # The function that uses three_line() three times in order to print 9 lines.

    three_lines()

    three_lines()

    three_lines()

    
def clear_screen(): # The function that uses three_lines() and nine_lines() twice and new_line once to print 25 lines. 

    three_lines()

    three_lines()

    nine_lines()

    nine_lines()

    new_line()

    
print ('calling nine_lines()') # Placeholder 1.

nine_lines() # calling the function that assigned to call fisrt.

print ('Printing twenty-five lines') # Placeholder 2.

clear_screen() # calling the second function that assigned to call.
