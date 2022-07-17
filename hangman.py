import random
from words import words1
from itertools import repeat
import string


def hangman():
    word = random.choice(words1).upper()
    word_letter = set(word)
    alphabet = set(string.ascii_letters.upper())
    used_letters = set()
    lives = 10
    while len(word_letter) > 0 and lives > 0:
        print(f'YOU HAVE {lives} LEFT AND  USED THESE LETTERS:', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word_letter]
        print('CURRENT WORDS:', ' '.join(word_list))
        user_letter = input('GUESS THE WORD: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives - 1
                print(f'HINT:THE WORD CONSISTS OF {len(word)} LETTERS ')
                print(f'THE FIRST WORD IS {word[0]} AND THE FOURTH WORD IS {word[4]}')
        elif user_letter in used_letters:
            print('YOU HAVE ALREADY USED THIS WORD')
        else:
            print('INVALID ENTRY')
    if lives == 0:
        print('SORRY BUT U ARE OUT OF CHANCES NOW ')
        print(f'BTW THE WORD WAS {word}')
    else:
        print('YAYY!!! YOU HAVE WON THE GAME')
        print(f'THE WORD WAS {word}')


name = input('PLEASE ENTER YOUR NAME TO START THE GAME>> ').upper()
print(f"HELLO {name}, I AM ASHAM YOU OPPONENT THIS MATCH")
print('I WILL CHOOSE A RANDOM WORD FOR YOU TRY TO GET IT CORRECT IN GIVEN CHANCES')
hangman()
print(f'HOPE YOU HAD FUN PLAYING WITH ME {name}')
a = 'LOL'
for i in repeat(a, 3):
    print(i)
