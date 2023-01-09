import random

answer = random.randint(1,100)

num_guess = 1

while True:
    guess = input('Am thinking of a number between 1 and 100. Take a guess. ')
    
    try:
        guess=int(guess)
    except:
        print('Invalid input')
        continue 
    #     
    if guess<=0:
        print('Your guess cannot be a negative number')
        continue 
    
     #
    if guess>100:
        print('Your guess cannot be a greater than 100')
        continue
    
    if num_guess < 10:
        if guess == answer:
            print('You win!')
            break
        
        elif guess < answer:
            print('Too low!')
        elif guess > answer:
            print('Too high!')
    
    else:
        num_guess = 0
        print('Next players turn')
        
    num_guess += 1
