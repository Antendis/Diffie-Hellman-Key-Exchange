from Crypto.Util import number
import random

prime = number.getPrime(2024) # Gets a random 64-bit prime number
print(f"Agreed upon prime: {prime}")

base_choices = [2, 3, 5]
base = random.choice(base_choices)  # Randomly choose a base from the list
print(f"Agreed upon base: {base}\n")

person_1_secret = random.randint(1, 20) 
person_2_secret = random.randint(1, 20) 

print(f"person 1's secret: {person_1_secret}")
print(f"person 2's secret: {person_2_secret}\n")

person_1_public = base ** person_1_secret % prime
person_2_public = base ** person_2_secret % prime

print(f"person 1's public key: {person_1_public}")
print(f"person 2's public key: {person_2_public}\n")

shared_secret = person_2_public ** person_1_secret % prime
shared_secret_check = person_1_public ** person_2_secret % prime

print(f"Shared secret: {shared_secret}")
print(f"Shared secret check: {shared_secret_check}\n")

if shared_secret == shared_secret_check:
    print("Shared secret successfully established!")
else:
    print("Shared secret mismatch, something went wrong!")