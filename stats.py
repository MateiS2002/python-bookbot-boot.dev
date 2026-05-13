from typing import List


def get_num_words(text: str):
    words: List[str] = text.split()
    word_count = len(words)

    return word_count


def get_char_count(text: str):
    chars_count = {}

    for char in text:
        lower_case_char : str  = char.lower()
        chars_count[lower_case_char] = chars_count.get(lower_case_char, 0) + 1
    return chars_count


def sort_on(char):
    return char["num"]


def get_sorted_list_of_dictionaries(text: str):
    sorted_list = []
    chars_count = get_char_count(text)

    for key in chars_count:
        entry = {"char": key,
                 "num": chars_count[key]}
        sorted_list.append(entry)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list