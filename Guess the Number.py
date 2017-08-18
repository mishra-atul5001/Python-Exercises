import random
score = 0

print('Guess a Number b/w 1 to 10,')
print('If your Guess is equal to Random Generated Number,')
print('+1 to your Score.')
for i in range(0,10):
    randomNumber = random.randint(1,5)
    print('guess a number between 1 and 5')
    yourGuess = int(input())
    randomNumber2 = random.randint(2,8)
    if yourGuess == randomNumber or yourGuess == randomNumber2:
        print('Amazing, Well done!')
        score = score + 1
        print('Current Score' + str(score))
    else:
        print('Nope, the number is ' + str(randomNumber))
        score = 0

print('Your score was ' + str(score) + ' out of 10')
