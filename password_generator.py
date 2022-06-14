import random

from _words import _words

class Allowed_Strings():
    words = _words
    special_characters = ["~", "!", "@", "#", "$", "%", "^", "*", "-", "_", "=", "+", "[", "{", "]", "}", "/", ";", ":", ",", ".", "?"]
    numbers = range(10)

def generate_password(iterations:int=4, *,
                    words:list[str]=Allowed_Strings.words,
                    special_characters:list[str]=Allowed_Strings.special_characters,
                    numbers:str=Allowed_Strings.numbers) -> str:

    password = []

    for i in range(iterations):
        word = random.choice(words).capitalize()
        special = random.choice(special_characters)
        number = random.choice(numbers)
        password.extend([word, special, number, ""])

    shuffled = random.sample(password, len(password)-1)

    return "".join(str(s) for s in shuffled)