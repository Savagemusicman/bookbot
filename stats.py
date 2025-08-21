def get_word_count(text):
    return len(text.split())


def character_count(text):
    char_dict = {}
    lowered_char = text.lower()

    for char in lowered_char:
        if char.isalpha():
            
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    return char_dict


def sort(character_count):
    sorted_dicts = []
    for char, count in character_count.items():
        new_dict = {"char": char, "num": count}
        sorted_dicts.append(new_dict)
    return sorted_dicts


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


# --- Example usage ---
text = "Hello world this is some test text for this app!"
print("Word count:", get_word_count(text))

char_dict = character_count(text)
print("Character counts:", char_dict)

sorted_list = chars_dict_to_sorted_list(char_dict)
print("Sorted list:", sorted_list)
