import random

answer = random.randint(1,100)



num_guess = 1


while True:
    guess = int(input('Take a guess. '))
    
    if num_guess < 10:
        if guess == answer:
            print('You win!')
            break
        
        
    
    num_guess += 1
