from goodreads import client
gc = client.GoodreadsClient("J7asX1xgQHBfotcBA4myA", "xJJdA53Ep3dowcwyP9wdOc7EY0LMflbKXvc0nVBw")
gc.authenticate("J7asX1xgQHBfotcBA4myA", "xJJdA53Ep3dowcwyP9wdOc7EY0LMflbKXvc0nVBw")

book = gc.book(1)
print(book.title)
authors = book.authors
print(authors[0].name)
print(book.average_rating)
