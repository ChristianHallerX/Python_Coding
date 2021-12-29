# -*- coding: utf-8 -*-
"""
Classes and inheritance.

Created on Wed Dec 29 01:26:43 2021
@author: Christian Haller
"""


# <codecell>Class Definition

import random

class Animal:
    """Basic class."""

    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name=""):
        self.name = new_name

    def __str__(self):
        return "animal:" + str(self.name) + " : " + str(self.age)


class Cat(Animal):
    """Cat class is a subclass of animal."""

    def speak(self):
        print('meow')

    def __str__(self):
        """Overwrite the Animal str method."""
        return "cat:" + str(self.name) + " : " + str(self.age)


class Person(Animal):
    """Person is a subclass of animal."""

    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")

    def __str__(self):
        """Overwrite the Animal str method."""
        return "person:" + str(self.name) + " : " + str(self.age)


class Student(Person):
    """Student is a subclass of Person."""

    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, new_major):
        self.major = new_major

    def speak(self):
        r = random.random()
        if r <= 0.25:
            print("I have homework.")
        elif 0.25 <= r < 0.5:
            print("I need sleep.")
        elif 0.5 <= r < 0.75:
            print("I should eat.")
        else:
            print("I am watching TV.")

    def __str__(self):
        """Overwrite the Animal str method."""
        return "student:" + str(self.name) + " : " + str(self.age) + " : "  \
            + str(self.major)


class Rabbit(Animal):
    """Rabbit is a sublcass of an Animal"""

    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def __str__(self):
        """Overwrite the Animal str method."""
        return "Rabbit: " + str(self.get_rid())

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        """Return same object as this class with age 0"""
        return Rabbit(age=0, parent1=self, parent2=other)

    def __eq__(self, other):
        """Compare two objects with the operator ==."""
        parents_same = self.parent1.rid == other.parent1.rid \
            and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
            and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite


# <codecell>Test Person
print("-----test Person subclass-----")
p1 = Person("Jack", 40)
p2 = Person("Geraldine", 90)

print(p1)

print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())

p1.speak()
p1.age_diff(p2)

# <codecell>Test Student
print("-----test Student subclass-----")

s1 = Student("Gavin", 33, "STEM")
s2 = Student("Julius", 66)
print(s1)
print(s2)
print(s1.get_name(), " says ", end=' ')
s1.speak()
print(s2.get_name(), " says ", end=" ")
s2.speak()

# <codecell>Test Rabbit
print("-----test Rabbit subclass-----")

r1 = Rabbit(age=3)
r2 = Rabbit(age=4)
r3 = Rabbit(age=7)
print("r1: ", r1)
print("r2: ", r2)
print("r3: ", r3)


# <codecell>Test Rabbit Addition
print("-----test Rabbit Addition-----")

r4 = r1 + r2
print("r4: ", r4)
print("r4 parent1:", r4.get_parent1())
print("r4 parent2:", r4.get_parent2())

# <codecell>Test Rabbit Equality/Parents
print("-----test Rabbit Equality/Parents-----")

r5 = r3 + r4
r6 = r4 + r3
print("r5 parent1: ", r5.get_parent1())
print("r5 parent2: ", r5.get_parent2())
print("r6 parent1: ", r6.get_parent1())
print("r6 parent2: ", r6.get_parent2())
print("r5 and r6 have the same parents?", r5 == r6)
print("r4 and r6 have the same parents?", r4 == r6)
