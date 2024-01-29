def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    num_letters = count_letters(book_text)
    print_report(book_path, num_words, num_letters)

def get_book_text(path):
        with open(path) as f:
            return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
     counter = dict()
     lowered = text.lower()
     for c in lowered:
          if c in counter:
               counter[c] += 1
          else:
               counter[c] = 1
        
     return counter

def print_report(book, words, letters):
     print("--- START ---")
     print(f"--- Report of {book}---")
     print(f"{words} words found in the document")
     print("")
     list_letters = list(letters)
     list_letters.sort()
     
     for c in range(len(list_letters)):
          if list_letters[c].isalpha():
               print(f"The '{list_letters[c]}' character was found {letters[list_letters[c]]} times")

     print("--- END ---")

main()