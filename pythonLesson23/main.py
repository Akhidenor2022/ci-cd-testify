
#1. Create a class called User
#2. Create a private attribute called __password with the value "password" in the User class
#3. Create a method get_password() that returns self.__password in the User class
#4. Create another class called ActiveUser that inherits from the User class
#5. Create a method get_password() that returns "********" in the ActiveUser class
#6. Instantiate an object of the ActiveUser class
# Print the value of get_password() from the object instance




class User:
    __password = "password"

    def get_password(self):
        return self.__password


class ActiveUser(User):
    def get_password(self):
        return "******"


online_user = ActiveUser()
print(online_user.get_password())