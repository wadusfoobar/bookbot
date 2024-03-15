import re

def main():
    book = "books/frankenstein.txt"
    text = contents(book)

    report(text, book)

def contents(book):
    with open(book) as f:
        return f.read()

def count_words(book):
    return len(book.split())

def count_letters(book):
    count = {}
    for c in book.lower():
        if re.match("[a-z]", c):
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
    return count

def letter_count_list_from_dict(dict):
    count = []
    for k, v in dict.items():
        count.append({"letter": k, "count": v})
    return count

def sort_on(letters):
    return letters["count"]

def report(text, book):
    print(f"--- Begin report of {book} ---")
    print(f"{count_words(text)} words found in the document\n")
    letters = letter_count_list_from_dict(count_letters(text))
    letters.sort(reverse=True, key=sort_on)
    for l in letters:
        print(f"The \'{l['letter']}\' was found {l['count']} times")
    print("--- End report ---")
main()
