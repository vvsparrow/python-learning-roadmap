text_string = input("Enter your text: ")
raw_words = text_string.split()
list_of_words = []

for word in raw_words:
    list_of_words.append(word)

if list_of_words:
    print(list_of_words[0], list_of_words[-1])
else:
    print("You forgot to enter text data.")
