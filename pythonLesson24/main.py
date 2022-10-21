#1. Create an abstract class called Vehicle
#2. Create an abstract method called drive_direction()
#3. Create another class Car that inherits from Vehicle
#4. Create another class Plane that inherits from Vehicle
#5. Try running the program and fix the abstract method issues
# Optionally instantiate the Car and Plane method, then invoke the drive_direction() in each of the object instances.
#Hint: the drive_direction() method in your Car should print "Drive forward", while drive_direction() in your Plane class should print "Drive Upward"



import abc



class VehicleElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def drive_direction(self):
        pass


class CarElement(VehicleElement):

    def drive_direction(self):
        return "Drive Forward"

class PlaneElement(VehicleElement):

        def drive_direction(self):
            return "Drive Upward"


car_element = CarElement()
print(car_element.drive_direction())

plane_element = PlaneElement()
print(plane_element.drive_direction())