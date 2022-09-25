"""
Factory Method is a Creational Design Pattern that allows an interface or a class to create an object, but lets subclasses decide which class or object to instantiate. 
Using the Factory method, we have the best ways to create an object. 
Here, objects are created without exposing the logic to the client, and for creating the new type of object, the client uses the same common interface.
"""

"""
img address: https://media.geeksforgeeks.org/wp-content/uploads/20200116152733/solution_factory-_diagram.png
"""

"""
Advantages of using Factory method: 

*We can easily add new types of products without disturbing the existing client code.
*Generally, tight coupling is being avoided between the products and the creator classes and objects.

Disadvantages of using Factory method:

*To create a particular concrete product object, the client might have to sub-class the creator class.
*You end up with a huge number of small files i.e, cluttering the files.
    *In a Graphics system, depending upon the user’s input it can draw different shapes like rectangles, Square, Circle, etc. 
    But for the ease of both developers as well as the client, we can use the factory method to create the instance depending upon the user’s input. 
    Then we don’t have to change the client code for adding a new shape.
    
    *On a Hotel booking site, we can book a slot for 1 room, 2 rooms, 3 rooms, etc. Here user can input the number of rooms he wants to book. 
    Using the factory method, we can create a factory class Any Rooms which will help us to create the instance depending upon the user’s input. 
    Again we don’t have to change the client’s code for adding the new facility.
"""
# Python Code for factory method
# it comes under the creational
# Design Pattern

class FrenchLocalizer:

	""" it simply returns the french version """

	def __init__(self):

		self.translations = {"car": "voiture", "bike": "bicyclette",
							"cycle":"cyclette"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class SpanishLocalizer:
	"""it simply returns the spanish version"""

	def __init__(self):
		self.translations = {"car": "coche", "bike": "bicicleta",
							"cycle":"ciclo"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class EnglishLocalizer:
	"""Simply return the same message"""

	def localize(self, msg):
		return msg

def Factory(language ="English"):

	"""Factory Method"""
	localizers = {
		"French": FrenchLocalizer,
		"English": EnglishLocalizer,
		"Spanish": SpanishLocalizer,
	}

	return localizers[language]()

if __name__ == "__main__":

	f = Factory("French")
	e = Factory("English")
	s = Factory("Spanish")

	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))

