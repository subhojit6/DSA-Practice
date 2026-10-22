class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Cow:
    def speak(self):
        print("Moo!")

class Duck:
    def speak(self):
        print("Quack!")

animals = [Dog(), Cat(), Cow(), Duck()]

for animal in animals:
    animal.speak()