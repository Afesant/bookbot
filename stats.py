def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count_dict = {}
    text = text.lower()

    for char in text:
        if char_count_dict.get(char):
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    
    return char_count_dict

def sort_on(item):
    return item[1]

def remove_non_alphanumeric(char_dict):
    return {k: v for k, v in char_dict.items() if k.isalpha()}

def get_sorted_char_count(char_dict):
    char_dict = remove_non_alphanumeric(char_dict)
    sorted_char_count = sorted(char_dict.items(), key=sort_on, reverse=True)
    return sorted_char_count