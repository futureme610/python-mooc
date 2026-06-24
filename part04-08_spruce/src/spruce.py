def spruce(size):
    print("a spruce!")

    max = 2*int(size)-1

    i = 0
    row = "*"

    while i < size:
        space = (max - len(row))//2
        combined = space * " " + row
        print(combined)
        row += "**"
        i += 1

    trunk = (max - 1)//2 
    print ((trunk * " ") + "*") 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)