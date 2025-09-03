class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'title: {self.title}, author: {self.author}, year: {self.year}'

def print_books_info(books):
    for book in books:
        print(book)

if __name__ == '__main__':
    books = [
        Book('The Richest Man in Babylon', 'George S. Clason', 1926),
        Book('Rich Dad Poor Dad', 'Robert Kiyosaki & Sharon Lechter', 1997)
    ]
    print_books_info(books)