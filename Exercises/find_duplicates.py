# Exercise: Check for duplicates in list with the help of a function:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

def duplicate_finder(list)
duplicates = []
    for item in list:
        if list.count(item) > 1:
            if item not in duplicates:
                duplicates.append(item)
    return duplicates       

print(duplicate_finder(some_list))
