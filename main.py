dictionary = {}

def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    print(f"There were {number_of_words(book_path)} words found in the document.")
    dictionaryA = number_of_letters(book_path)
    print(sorts(dictionaryA))
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(path):
    with open(path) as f:
        file_contents = f.read()
        split_file = file_contents.split()
        counter = 0
        for word in split_file:
            counter +=1
        return counter
    
def number_of_letters(path):
    with open(path) as f:
        file_contentss = f.read()
        file_contents = file_contentss.lower()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for letter in alphabet:
            dictionary[letter] = file_contents.count(letter)
        return dictionary

def sorts(dictionary):
    new_list = []
    for char,count in dictionary.items():
        new_dict = {'char': char, 'num': count}
        new_list.append(new_dict)
    return new_list
        

       


main()