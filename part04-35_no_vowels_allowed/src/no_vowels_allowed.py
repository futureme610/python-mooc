def no_vowels(word):
    new_word = ""
    vowels = "aeiou"
    i = 0
    while i < len(word):
        if word[i] not in vowels:
            new_word += word[i]
        i += 1
    return new_word

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))    