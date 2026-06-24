def factorials(n: int):
    #return factorials of the number 1 to n
    
    my_dictionary = {}

    result = 1
    for i in range(1, n + 1):
        result *= i    
        my_dictionary[i] = result

    return my_dictionary

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5]) 