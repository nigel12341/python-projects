import time

str = ""
alphabet = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
fullAlphabet = str.join(alphabet)
search = input("")

print(fullAlphabet.find(search) + 1)
time.sleep(5000)