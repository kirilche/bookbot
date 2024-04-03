from string import ascii_lowercase
from collections import Counter


def count_words(string:str) -> int:
    return len(string.split())


def count_letters_case_insensitive(string:str) -> dict:
    count = Counter(string)
    result = {}
    for letter in ascii_lowercase:
        result[letter] = count[letter] + count[letter.upper()]
    return result


def print_report(path:str,file_contents:str) -> None:
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()
    the_dict = count_letters_case_insensitive(file_contents)
    sort_dict = dict(sorted(the_dict.items(), key = lambda item: item[1], reverse=True))
    for key in sort_dict:
        print(f"The '{key}' character was found {the_dict[key]} times")
    print("--- End report ---")


def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        print_report(path, file_contents)



if __name__ == "__main__":
    main()