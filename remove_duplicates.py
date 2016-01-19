def remove_duplicates(string):
    unique_characters = set()
    result_string = ""
    for char in string:
        if char not in unique_characters:
            unique_characters.add(char)
            result_string += char
    return result_string

print remove_duplicates("tree traversal")
