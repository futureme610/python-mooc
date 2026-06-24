def read_fruits():
    # reads the file and returns a dictionary based on the contents
    # the name of the fruit should be the key
    # the value should be its price
    # prices should be float
    fruit_prices = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit_prices[parts[0]] = float(parts[1])
    
    return fruit_prices
if __name__ == "__main__":
    read_fruits()
