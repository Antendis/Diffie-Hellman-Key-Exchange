from Crypto.Util import number

prime = number.getPrime(64) # Gets a random 64-bit prime number
print(f"Agreed upon prime: {prime}")