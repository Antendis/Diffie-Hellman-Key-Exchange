from Crypto.Util import number
import random

prime = number.getPrime(64) # Gets a random 64-bit prime number
print(f"Agreed upon prime: {prime}")

base_choices = [2, 3, 5]
base = random.choice(base_choices)  # Randomly choose a base from the list
print(f"Agreed upon base: {base}\n")

person_1_secret = random.randint(1, 20) 
person_2_secret = random.randint(1, 20) 

print(f"person 1's secret: {person_1_secret}")
print(f"person 2's secret: {person_2_secret}")

