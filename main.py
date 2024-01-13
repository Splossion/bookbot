def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found on the document\n")
    print_report(count_letters(text))
    print("--- End report ---")    

def read_book(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents

def count_words(string: str) -> int:
    return len(string.split())

def count_letters(string: str) -> dict:
    string = string.lower()
    letters_dict = {}
    for x in string:
        if x not in letters_dict:
            letters_dict[x] = 1
        else:
            letters_dict[x] += 1
    return letters_dict

def print_report(letters_dict):
    letters_list = []
    for letter in letters_dict:
        if letter.isalpha():
            letters_list.append(letter)
    letters_list.sort()
    for letter in letters_list:
        print(f"The '{letter}' character was found {letters_dict[letter]} times")

if __name__ == "__main__":
    main()