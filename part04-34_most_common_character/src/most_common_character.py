def most_common_character(word):
    biggest = word[0]
    i = 0
    while i < len(word):
 
        if word.count(word[i]) > word.count(biggest):
            biggest = word[i]
        i += 1

    return biggest
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))


    # Write your solution here