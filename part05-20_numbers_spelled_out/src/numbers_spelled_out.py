

def dict_of_numbers():
    #returns a new dictionary
    #the dictionary should have the numbers from 0 to 99 as its keys
    #the value attached to each key should be the number spelled out in words.
    
    ones = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
    }

    tens = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
    }
    
    numbers = {}
    for key, value in ones.items():
        numbers[key] = value
    
    for key, value in tens.items():
        numbers[key] = value
    
    for ten in range(20,100,10):
        for one in range(1,10):
            number = ten + one
            numbers[number] = tens[ten] + "-" + ones[one]

    return numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
