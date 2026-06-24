def anagrams(string1, string2):
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)

    if sorted_string1 == sorted_string2:
        return True
    
    else:
        return False

if __name__ == "__main__":
    anagrams("aidan", "nadia")