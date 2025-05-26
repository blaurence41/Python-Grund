word_without_vowels = ""

user_word = input("I am still hungry, more words, please: ")# Prompt the user to enter a word
user_word = user_word.upper()                                        # and assign it to the user_word variable.

user_word_list = list(user_word)
for letter in user_word:
    if letter == "A":
        user_word_list.remove(letter)
        continue
    elif letter == "E":
        user_word_list.remove(letter)
        continue
    elif letter == "I":
        user_word_list.remove(letter)
        continue
    elif letter == "O":
        user_word_list.remove(letter)
        continue
    elif letter == "U":
        user_word_list.remove(letter)
        continue
else:
    for letter in user_word_list:
        word_without_vowels += letter 
    print(word_without_vowels)
    
# Print the word assigned to word_without_vowels.