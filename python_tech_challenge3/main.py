# Using the OOP feature Inheritance, create a class Animal with the method sound()
# then create a Cat and Dog class that inherits from the Animal class. The Cat and Dog class should override the sound class and
# print a different sound


class Animal:
    def sound(self):
        ani_sound = "Moo"
        return ani_sound


class Tiger(Animal):
    def sound(self):
        ani_sound = "Roar"
        return ani_sound


class Monkey(Animal):
    def sound(self):
        ani_sound = "Whoop"
        return ani_sound


tiger_sound = Tiger()
monkey_sound = Monkey()
print("Tiger says: ", tiger_sound.sound())
print("Monkey says: ", monkey_sound.sound())