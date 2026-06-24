# Write your solution here
def same_chars(input, a, b):
    if a >= len(input) or b >= len(input):
        return False
    
    else:
        if input[a] == input[b]:
            return True

        else:
            return False
    
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))