class Ebook():
    def __init__(self, title, author, number_of_pages, current_page):
        self.is_open = False
        self.title = title
        self.author = author
        self.pages = number_of_pages
        self.now_at = current_page

    def open_book(self):
        '''opens book'''
        self.is_open = True

    def close_book(self):
        '''closes book'''
        self.is_open = False

    def next_page(self):
        '''turns to the next page'''
        if self.now_at < self.pages and self.is_open == True:
            self.now_at += 1
    
    def prev_page(self):
        '''turns to previous page'''
        if self.now_at > 0 and self.is_open == True:
            self.now_at -= 1

    def book_status(self):
        '''prints basic information about the book'''
        if self.is_open == True:
            print(f'Author: {self.author}, Title: {self.title}, Number of pages: {self.pages}, Currently at page: {self.now_at}')
        else:
            print("Book is closed")

        