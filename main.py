import sys
from stats import get_num_words,get_sorted_list_of_dictionaries


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_argument = sys.argv[1]

    try:
        book_string = get_book_text(path_argument)
    except FileNotFoundError:
        print("Invalid file path, no txt file found")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_argument}")

    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_string)} total words")
    print("--------- Character Count -------")

    for item in get_sorted_list_of_dictionaries(book_string):
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def get_book_text(path_to_file: str):
    with open(path_to_file, encoding="utf-8-sig") as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    main()