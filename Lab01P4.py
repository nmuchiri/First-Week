# Naomi Muchiri
# Date: 08/23/2026
# A program to calculate the cost of total purchase

# Price Structure - Input

books_price = 3.25
DVDs_price = 4.50
games_price= 6.25
tax = 0.07

# Processing

books = int(input('Enter number of books: '))
DVDs = int(input('Enter number of DVDs: '))
games = int(input('Enter number of games: '))

cost_before_tax = (books_price * books) + (DVDs_price * DVDs) + (games_price *games)
print(f"The cost before tax is: {cost_before_tax}")
sales_tax = cost_before_tax * tax
print(f"The sales tax is: {sales_tax }")

cost_after_tax = sales_tax + cost_before_tax
print(f"The cost after tax is: {cost_after_tax}")
