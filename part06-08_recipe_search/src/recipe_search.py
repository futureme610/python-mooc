# Write your solution here
def list_format(filename: str):
    recipe_list = []
    recipe_row = []
    with open(filename) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            if line != "":
                recipe_row.append(line)
            else:
                recipe_list.append(recipe_row)
                recipe_row = []
        if recipe_row:
            recipe_list.append(recipe_row)
    return recipe_list
    
def search_by_name(filename: str, word: str):
    # go through the file and select all recipes whose name contains the given search string
    # the names of these recipes are then returned in a list
    recipe_list = list_format(filename)
    search_list = []
    for row in recipe_list:
        if word.lower() in row[0].lower():
            search_list.append(row[0])
    return search_list

def search_by_time(filename: str, prep_time: int):
    # go through the file and select all recipes whose prepartion time is at most the number given
    recipe_list = list_format(filename)
    recipe_time = []
    for row in recipe_list:
        if prep_time >= int(row[1]):
            recipe_time.append(f"{row[0]}, preparation time {row[1]} min")
    return recipe_time

if __name__ == "__main__":
    print(search_by_name("recipes1.txt", "cake"))
    found_recipes = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)