text_input = input("Write text: ")
all_words = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        all_words.append(line)

for word in text_input.split():
    if word.lower() not in all_words:
        starred_word = f"*{word}*"
        text_input = text_input.replace(word, starred_word)

print(text_input)


# write your solution here
