import ebook

a = ebook.Ebook("Hobbit", "J.R.R Tolkien", 328, 12)

a.open_book()
a.book_status()
for n in range(12):
    a.next_page()
a.book_status()
a.close_book()
a.book_status()
for n in range(12):
    a.prev_page()
a.book_status()
a.open_book()
a.book_status()