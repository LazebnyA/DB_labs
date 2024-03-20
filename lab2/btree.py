def name_hash(name):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hash_value = 0

    for char in name.lower():
        if char.isalpha():
            index = alphabet.index(char) + 1
            hash_value += index

    return hash_value


def find_names_after(name, name_list):
    name_hash_value = name_hash(name)
    names_after = []

    for other_name in name_list:
        if name_hash(other_name) > name_hash_value:
            names_after.append(other_name)

    return names_after


# Приклад використання:
names = ["John", "Alice", "Bob", "Eva", "Charlie"]

hashes = map(name_hash, names)

print(list(zip(names, hashes)))

print(find_names_after("Bob", names))
