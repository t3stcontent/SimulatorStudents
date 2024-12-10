#Task1
user_input = input("Enter text ")
print(user_input[::-1])

#Task2
user_input = input("Enter text ")
letter_count = sum(char.isalpha() for char in user_input)
nums_counts = sum(char.isdigit() for char in user_input)

print(f"Count literals = {letter_count} Numbers: {nums_counts}")

#Task3
user_input = input("Enter text ")
search_char = input("Enter char: ")

char_count = user_input.count(search_char)
print(f"symbol {search_char} {char_count} times")

#Task4
user_input = input("Enter text ")
search_word = input("Enter word: ")

word_count = user_input.split().count(search_word)
print(f"Word {search_word} {word_count} times")

#Task5
user_input = input("Enter text ")
search_word = input("Enter sear word ")
replase_word = input("Enter replace word ")

modify_string = user_input.replace(search_word, replase_word)
print("List after excjanche = ", modify_string)