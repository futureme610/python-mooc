def line(length, input):
    
    if input == "":
        input = "*"
    print(input[0] * length)

def shape(size, character1, width, character2):
    i = 1
    while i <= size:
        line(i, character1)
        i+=1
    
    while i <= size + width:
        line(size, character2)
        i+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")