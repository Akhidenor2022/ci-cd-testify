
# 1. Create a class called Human
# 2. Initialize the class

class Human:

    name = "girl"
    group = "Mammal"

    def get_name_grou(self):
        return self.name + ":" + self.group

# objects
girl = Human()
print(girl.name, girl.group, girl.get_name_grou())
