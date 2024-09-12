class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.set_author(author)
        self.set_book(book)
        self.set_date(date)
        self.set_royalties(royalties)
        Contract.all.append(self)

    def set_author(self, author):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        self.author = author

    def set_book(self, book):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        self.book = book

    def set_date(self, date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        self.date = date

    def set_royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        self.royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]