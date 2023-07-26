from random import randint
sekred_code = str(randint(10000,100000))
while True:
    if len(sekred_code)==len(set(sekred_code)):
        break
    sekred_code = str(randint(10000,100000))
user_code= input('ваше число: ')
while user_code!=sekred_code:
    if user_code == 'сдаюсь':
        print(sekred_code)
        exit()
    elif user_code == 'помоги':
        clue = ['*'] * len(sekred_code)
        random_pos = randint(0, len(sekred_code))
        clue[random_pos] = sekred_code[random_pos]
        clue = ''.join(clue)
        print(clue)
    else:
        bulls=0
        cows=0
        for i in range(len(sekred_code)):
            if user_code[i] == sekred_code[i]:
                bulls += 1
            elif user_code[i] in sekred_code:
                cows += 1
        print(f'Быков: {bulls}  Коров: {cows}')

    user_code = input('ваше число: ')
print('победа!')