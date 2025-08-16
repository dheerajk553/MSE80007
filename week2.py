
import random
import string
def blanks(len):

    letter = string.ascii_lowercase
    return ''.join(random.choice(letter) 
                   for _ in range(len))
    print("enter any name or type any anything")
totalruntime=5
word = blanks(6)
# Create blanks for each letter
blanks = "_ " * len(word)
print("Random word:", word)
print("Blanks:     ", blanks.strip())
#print("gusee the word")
#print("ok")
#for i in range(5):
#print(i)
        