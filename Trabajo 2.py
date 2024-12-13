import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = int(input("Presente la longitud de tu contraseña"))
result = ""
for i in range(password):
    result += random.choice(characters)
print(result)