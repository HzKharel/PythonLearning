
def sum(a, b, c = 0):
    return a+b+c

print(sum(1,3,6))


class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def set_age(self, age):
        self._age = age
    def __str__(self):
        return "Dog: " + self._name + " age: " + str(self._age)
    def random():
        return  7

d1 = Dog("Max",4)
print(d1)
print(Dog.random())