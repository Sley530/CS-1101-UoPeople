# The recursive function countdown
def countdown(n):
        if n <= 0:
            print('Blastoff!')
        else:
            print(n)
            countdown(n-1)
        
# The new recursive function countup          
def countup(n):
        if n >= 0:
            print('Blastoff!')
        else:
            print(n)
            countup(n+1)

# The programs that gets a number using keyboard input.

n = int(input('Enter number here:'))
if n > 0:
    countdown(n)
elif n < 0:
    countup(n)
else:
    countup(n)
    
    
    
# My own function that has a runtime error

def myfunct(p):
       if p <= 0:
            print('GREAT!')
       else: 
            print(p)
            myfunct(p//1)
            
myfunct(7)

        
