import random
import time
from colorama import init, Fore
from text_in_sound import text_sound


# counter words (50sec)
counter_words = 10

# waiting time between words
time_word = 10

# colorama init
init(autoreset=True)


# open, read txt (17mb)
with open('russian.txt', 'r') as file:
    words = file.readlines()
    words = [s.strip("\n") for s in words]


# random word in console and text to speech translation
def random_word(words):
    top_counter = 1
    for i in range(counter_words):
        color_text = Fore.BLUE, Fore.GREEN, Fore.RED
        rand_color_text = random.choice(color_text)
        my_word = random.choice(words)
        # console interface
        print(('*' * counter_words) + ' ' + str(top_counter) + ' ' + ('*' * counter_words))
        print(rand_color_text + my_word)
        print()
        top_counter += 1
        text_sound(my_word)
        time.sleep(time_word)


random_word(words)










