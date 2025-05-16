books = []
pages = []
total_pages = 0
while True:
    book_name = input("Enter a book name: ")
    if book_name.lower() == "q":
        break
    books.append(book_name)
    page_num = int(input("How many pages have you read?: "))
    pages.append(page_num)
print("\n----Your reading list ----")
for book in books:
    print(f"- {book}")
total_books=len(books)
total_pages=sum(pages)
print(f"Total pages: {total_pages}")
print(f"Total books: {total_books}")


