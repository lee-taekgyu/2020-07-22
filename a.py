class C():
    def __init__(self):
        print("instanc of class c was made")
        self.name = "ccc"
        self.age = 0

    def say_hi(self):
        print('hi')

    def add_age(self, n :int):
        self.age += n

    def __str__(self):
        return "__str__call"

    def __repr__(self):
        return "__repr__call"

    def __abs__(self):
        print("__abs__ call")

    def __len__(self):
        print("__len__ call")

    def __add__(self, other):
        return self.age + other.age
