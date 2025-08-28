# -------------------------------
# Assignment 1: Design Your Own Class
# -------------------------------

# Parent class
class Book:
    def __init__(self, title, author, pages):
        # attributes
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages.")

    def read(self):
        print(f"You start reading '{self.title}'... 📖")


# Child class (inheritance)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        # call parent constructor
        super().__init__(title, author, pages)
        self.file_size = file_size

    # method overriding (polymorphism)
    def read(self):
        print(f"You are reading '{self.title}' on your tablet. 💻 (File size: {self.file_size}MB)")


# Create objects
book1 = Book("The River Between", "Ngugi wa Thiong'o", 200)
ebook1 = EBook("Python for Starters", "Ann Miano", 120, 5)

book1.description()
book1.read()

ebook1.description()
ebook1.read()

print("\n")  # just spacing

# -------------------------------
# Activity 2: Polymorphism Challenge
# -------------------------------

class Animal:
    def move(self):
        # generic action
        print("This animal moves somehow.")

class Dog(Animal):
    def move(self):
        print("The dog runs on four legs. 🐕")

class Bird(Animal):
    def move(self):
        print("The bird flies in the sky. 🐦")

class Fish(Animal):
    def move(self):
        print("The fish swims in water. 🐟")


# Create a list of animals
animals = [Dog(), Bird(), Fish()]

# Loop through them and call move()
for a in animals:
    a.move()
