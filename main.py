from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_char_count

import sys

def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        book_text = get_book_text(path_to_file)
        word_count = get_num_words(book_text)
        char_count_dict = get_char_count(book_text)
        sorted_char_count = get_sorted_char_count(char_count_dict)

        print('============ BOOKBOT ============')
        print('Analyzing book found at books/frankenstein.txt...')
        print('----------- Word Count ----------')
        print(f'Found {word_count} total words.')
        print('--------- Character Count -------')
        for char, count in sorted_char_count:
            print(f"{char}: {count}")


if __name__ == "__main__":
    main()