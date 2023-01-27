# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
# con el alfabeto y los números en "leet".
# (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#

def leet(normal_word: str):

    leet_word = ""

    for letter in normal_word:
        if letter == "a":
            leet_word += "4"
        else:

            leet_word += letter
    
    return leet_word


if __name__ == '__main__':
    print(leet("holaaaa"))