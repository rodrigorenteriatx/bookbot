def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(get_dict_letters(text))
    print_report(text, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_dict_letters(text):
    letters_count = {}
    for char in text:
        #Returns True if all characters in the string are in the alphabet
        if char.isalpha():
            char = char.lower()
            if char in letters_count:
                letters_count[char] += 1
            else:
                letters_count[char] = 1
    return letters_count

def print_report(text, book_path):
    num_words = get_num_words(text)
    letters = get_dict_letters(text)
    # items() -> returns a list containing dictionary keys
    sorted_items = dict(sorted(letters.items() , key=lambda letter: letter[1], reverse=True))
    
    print(f"--- Begin report of {book_path} ---\n")
    print(f"{num_words} words found in the document")

    for k,v in sorted_items.items():
        print(f"The '{k}' character was found {v} times")

    print("--- End report ---")
    

    
main()