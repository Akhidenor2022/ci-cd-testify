#1. Create a class called Human
#2. Add an attribute leg_count with the value of 4
#3. Add a method called get_gender() that returns "Unknown" in the Human class
#4. Create another class called Man that extends Human
# Optionally you can instantiate the classes Man and Woman
# then print out the values of the get_gender() method in each object instance



class Human:
    leg_count = 4
    gender = "Unknown"

    def get_gender(self):
        print("Gender: {", self.gender + " }")


class Man(Human):

    def __init__(self, gender):
        self.gender = gender


class Woman(Human):

    def __init__(self, gender):
        self.gender = gender


gender1 = Human()
gender1.get_gender()

man1 = Man("Male")
man1.get_gender()

woman1 = Woman("Female")
woman1.get_gender()






