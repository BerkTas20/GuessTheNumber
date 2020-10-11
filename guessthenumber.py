import random
import time

 
print  ('<<<<<Welcome to guess the number game>>>>>>  ')

number = random.randint(1,100)

right_to_predict = 12


while True:
    guess = int(input('your guess: '))

    if guess == number:
        print(' the forecast is being questioned...')
        time.sleep(2)
        print('Congratulations! Successful')

        break
    
    elif guess > number:
        print(' the forecast is being questioned...')
        time.sleep(2)
        right_to_predict-=1
        print('Please enter a smaller number')
        print('remaining forecast: ',right_to_predict)

    else:
        print(' the forecast is being questioned...')
        time.sleep(2)
        right_to_predict-=1
        print('Please enter a bigger number')
        print('remaining forecast: ',right_to_predict)

    if right_to_predict == 0:
        print('your guess is over')
        print('prediction of the computer',number)

        break





    
    



