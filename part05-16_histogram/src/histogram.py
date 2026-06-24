def histogram(word: str):
    #print out a histogram representing the number of times each letter occurs in the string.
    #each occurrence of a letter should be represented by a star on the specific line for that letter.
    groups = {}
    for letter in word:
        if letter not in groups:
            groups[letter] = 0
        groups[letter] += 1
    for key, value in groups.items():
        stars = value * "*"
        print(f"{key} {stars}")

if __name__ == "__main__":
    groups = histogram("abba")