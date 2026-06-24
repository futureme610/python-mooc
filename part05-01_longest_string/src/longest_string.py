# Write your solution here
def longest(words: list):
    long_word = ""
    for word in words:
        if len(word) >= len(long_word):
            long_word = word
    return long_word

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings)) 