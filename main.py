import random
import time
from text_in_sound import text_sound


# Counter words
count_words = 10

# open txt (17mb)
with open('russian.txt', 'r') as file:
    words = file.readlines()
    words = [s.strip("\n") for s in words]


# random word and text to speech translation
def random_word(words):
    for i in range(count_words):
        my_word = random.choice(words)
        print(my_word)
        text_sound(my_word)
        time.sleep(10)


random_word(words)










