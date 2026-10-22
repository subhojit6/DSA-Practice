class Animal:
    def eat(self):
        print("This animal eats.")

class Dog(Animal):
    def eat(self):
        super().eat()
        print("The dog is eating dog food.")

    def bark(self):
        print("It says Woof!")

class Cat(Animal):
    def meow(self):
        print("It says Meow!")

dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()