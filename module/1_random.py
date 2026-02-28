import random

print("one random number betweer 0 and 1 :",random.random())
print("one random float number betwwen 1 to 100 :",random.uniform(1,100))
print("one int number betwweb 1 to 100 :",random.randint(1,100))

books = ["Python Crash Course", "Fluent Python", "Learning Python", "Python for Data Analysis", "Automate the Boring Stuff with Python", "Effective Python", "Python Tricks", "Clean Code in Python", "Mastering Python Regular Expressions", "Python Cookbook", "Advanced Python Programming", "Test Driven Development with Python", "Two Scoops of Django", "Python for Finance", "Natural Language Processing with Python", "Machine Learning with Python", "Python Deep Learning", "The Pragmatic Programmer", "Design Patterns in Python", "Real Python"]
print("pick one random python book :",random.choice(books))
print("pick two random python book :",random.choices(books,k=2))


