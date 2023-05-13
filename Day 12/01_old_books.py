name = input()
books_checked = 0

while True:
    current_book = input()
    if current_book == 'No More Books':
        print(f'The book you search is not here!\nYou checked {books_checked} books.')
        break
    elif current_book != name:
        books_checked += 1
    elif current_book == name:
        print(f'You checked {books_checked} books and found it.')
        break
