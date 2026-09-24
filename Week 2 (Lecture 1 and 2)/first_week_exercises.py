from os import name
from platform import processor


class Book:
    #"""the init dunder method"""
    def __init__(self, name, author, price, pages):
        self.name = name
        self.author = author
        self.price = price
        self.pages = pages
    #"""the str dunder method"""
    def __str__(self):
        return f'the book {self.name} was written by {self.author}'
    #"""the repr dunder method"""
    def __repr__(self):
        return f"Book(title = '{self.name}', author = '{self.author}', price = '{self.price}'"
    # """the eq dunder method"""
    def __eq__(self, other):
        if not (isinstance(other, Book)):
            return False
        return self.name == other.name and self.author == other.author
    # """the lt dunder method"""
    def __lt__(self, other):
        if not isinstance(other, Book):
            return False
        return self.price < other.price
    # """the len dunder method"""
    def __len__(self):
        return self.pages



book1 = Book('book1', 'author1', 20000, 5000)
book2 = Book('book1', 'author1', 20000, 5000)

#str
print(book1)
print(str(book1))

#repr
print(repr(book1))

#eq
print(book1 == book2)

#lt
print(book1 < book2)

#len
print(len(book1))



print("==========================================================================================================")

#Composition Example (TV has remote)

class Remote:
    def channelUp(self):
        return "channel upped by 1"

class TV:
    def __init__(self, name):
        self.remote = Remote()
        self.name = name
    def channelUp(self):
        return self.remote.channelUp()

tv = TV('samsung')
print(tv.channelUp())

print("==========================================================================================================")

# demonstrating MRO in python

class A:
    def show(self):
        return "show A"

class B(A):
    pass

class C:
    def show(self):
        return "show C"

class D(B, C):
    pass

print(D.mro())
print(D().show())