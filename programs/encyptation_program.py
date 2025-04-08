import random
import string

chars = list(" " + string.ascii_letters + string.digits + string.punctuation)


shuffled_chars = chars.copy()
random.shuffle(shuffled_chars)


word = input("Enter a word to shuffle: ")
new_word_encrypted = ""

for char in word:
    index = chars.index(char) #return the index in the chars list of each char in the word
    new_word_encrypted += shuffled_chars[index]


print(f"Your encryppted word  is: {new_word_encrypted}")
    

#Decryption:

word_decrypted = ""
for c in new_word_encrypted:
    index = shuffled_chars.index(c) #return the index in the shuffled chars list of each char in the word
    word_decrypted += chars[index]


print(f"Your decryppted word is: {word_decrypted}") 