class Animal:
    name = color = ""

    def __init__(self, animal_name, animal_color):
        self.name = animal_name
        self.color = animal_color
    def makeSound(self, sound):
        print(self.name, "is", sound)
    def eat(self, food):
         print(self.name, "is eating", food)   

cat = Animal("Max", "yellow")
cat.makeSound("meowing")
cat.eat("fish")

cat = Animal("Miu", "grey")
cat.makeSound("barking")
cat.eat("snacks")  

bird = Animal("Tweety", "blue")
cat.makeSound("chirping")
cat.eat("corn")         