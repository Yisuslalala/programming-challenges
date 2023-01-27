import string
import random

# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# Longitud: Entre 8 y 16.
# Con o sin letras mayúsculas.
# Con o sin números.
# Con o sin símbolos.
# Pudiendo combinar todos estos parámetros entre ellos)

def password_generator(max_letras: int, mayus: bool, nums: bool, simbolos: bool):
    print("Generador de contraseñas")
    letras = string.ascii_letters
    password = "".join(random.choice(letras) for i in range(max_letras - 2)).lower() 
    
    if mayus:
        password.upper()

    if nums:
        letras = letras + string.digits 

    if simbolos:
        letras = letras + string.punctuation

    password = "".join(random.choice(letras) for i in range(max_letras - 2))
    print(f"La contraseña es : {password}")


if __name__ == '__main__':
    password_generator(10, True, True, True)
    password_generator(10, True, False, False)
    password_generator(10, False, 1, 0)