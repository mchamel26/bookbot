
chars = "abcdefghijklmopqrstuvwyxz"

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)

    print(f"--- Begin report of {book_path}")
    print(f"{word_count} words found in the document")
    print("")
    ordered_char_count = dict(sorted(char_count.items(),key=lambda item: -item[1]))
    for k in ordered_char_count:
        if k.isalpha():
            print(f"The '{k}' character was found {ordered_char_count[k]} times")
        else: 
            next
    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        #...
        return f.read()

def get_word_count(contents):
    words = contents.split()
    return len(words)

def get_char_count(contents):
    chars = {}
    for c in contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars



main()



