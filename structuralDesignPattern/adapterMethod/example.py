# Dog - Cycle
# human - Truck
# car - Car
"""
Adapter method is a Structural Design Pattern which helps us in making the incompatible objects adaptable to each other. 
The Adapter method is one of the easiest methods to understand because we have a lot of real-life examples that show the analogy with it. 
The main purpose of this method is to create a bridge between two incompatible interfaces. This method provides a different interface for a class. 
We can more easily understand the concept by thinking about the Cable Adapter that allows us to charge a phone somewhere that has outlets in different shapes. 
Using this idea, we can integrate the classes that couldn’t be integrated due to interface incompatibility.
"""

"""
Advantages

Principle of Single Responsibility: We can achieve the principle of Single responsibility with Adapter Method because here we can separate the concrete code from the primary logic of the client.
Flexibility: Adapter Method helps in achieving the flexibility and reusability of the code.
Less complicated class: Our client class is not complicated by having to use a different interface and can use polymorphism to swap between different implementations of adapters.
Open/Closed principle: We can introduce the new adapter classes into the code without violating the Open/Closed principle.

Disadvantages

Complexity of the Code: As we have introduced the set of new classes, objects and interfaces, the complexity of or code definitely rises.
Adaptability: Most of the times, we require many adaptations with the adaptee chain to reach the compatibility what we want.

Applicability

To make classes and interfaces compatible : Adapter method is always used when we are in need to make certain classes compatible to communicate.
Relatable to Inheritance: When we want to reuse some piece of code i.e., classes and interfaces that lack some functionalities, it can be done using the Adapter Method.

"""
class MotorCycle:

	"""Class for MotorCycle"""

	def __init__(self):
		self.name = "MotorCycle"

	def TwoWheeler(self):
		return "TwoWheeler"


class Truck:

	"""Class for Truck"""

	def __init__(self):
		self.name = "Truck"

	def EightWheeler(self):
		return "EightWheeler"


class Car:

	"""Class for Car"""

	def __init__(self):
		self.name = "Car"

	def FourWheeler(self):
		return "FourWheeler"

class Adapter:
	"""
	Adapts an object by replacing methods.
	Usage:
	motorCycle = MotorCycle()
	motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
	"""

	def __init__(self, obj, **adapted_methods):
		"""We set the adapted methods in the object's dict"""
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __getattr__(self, attr):
		"""All non-adapted calls are passed to the object"""
		return getattr(self.obj, attr)

	def original_dict(self):
		"""Print original object dict"""
		return self.obj.__dict__


""" main method """
if __name__ == "__main__":
    
    """list to store objects"""
    objects = []
    
    motorCycle = MotorCycle()
    objects.append(Adapter(motorCycle, wheels = motorCycle.TwoWheeler))
    
    truck = Truck()
    objects.append(Adapter(truck, wheels = truck.EightWheeler))
    
    car = Car()
    objects.append(Adapter(car, wheels = car.FourWheeler))
    for obj in objects:
        print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))

