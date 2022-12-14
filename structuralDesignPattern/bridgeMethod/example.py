"""
The bridge method is a Structural Design Pattern that allows us to separate the Implementation Specific Abstractions and Implementation Independent Abstractions from each other and can be developed considering as single entities.
The bridge Method is always considered as one of the best methods to organize the class hierarchy.

"""

"""

Advantages

Single Responsibility Principle: The bridge method clearly follows the Single Responsibility principle as it decouples an abstraction from its implementation so that the two can vary independently.
Open/Closed Principle: It does not violate the Open/Closed principle because at any time we can introduce the new abstractions and implementations independently from each other
Platform independent feature: Bridge Method can be easily used for implementing the platform-independent features.

Disadvantages

Complexity: Our code might become complex after applying the Bridge method because we are intruding on new abstraction classes and interfaces.
Double Indirection: The bridge method might have a slight negative impact on the performance because the abstraction needs to pass messages along with the implementation for the operation to get executed.
Interfaces with only a single implementation: If we have only limited interfaces, then it doesn’t sweat a breath but if you have an exploded set of interfaces with minimal or only one implementation it becomes hard to manage

Applicability

Run-time Binding: Generally Bridge method is used to provide the run-time binding of the implementation, here run-time binding refers to what we can call a method at run-time instead of compile-time.
Mapping classes: The bridge method is used to map the orthogonal class hierarchies
UI Environment: A real-life application of the Bridge method is used in the definition of shapes in a UI Environment

"""



"""Code implemented with Bridge Method.
We have a Cuboid class having three attributes
named as length, breadth, and height and three
methods named as produceWithAPIOne(), produceWithAPItwo(),
and expand(). Our purpose is to separate out implementation
specific abstraction from implementation-independent
abstraction"""

class ProducingAPI1:

	"""Implementation specific Abstraction"""

	def produceCuboid(self, length, breadth, height):

		print(f'API1 is producing Cuboid with length = {length}, '
			f' Breadth = {breadth} and Height = {height}')

class ProducingAPI2:

	"""Implementation specific Abstraction"""

	def produceCuboid(self, length, breadth, height):

		print(f'API2 is producing Cuboid with length = {length}, '
			f' Breadth = {breadth} and Height = {height}')

class Cuboid:

	def __init__(self, length, breadth, height, producingAPI):

		"""Initialize the necessary attributes
		Implementation independent Abstraction"""

		self._length = length
		self._breadth = breadth
		self._height = height

		self._producingAPI = producingAPI

	def produce(self):

		"""Implementation specific Abstraction"""

		self._producingAPI.produceCuboid(self._length, self._breadth, self._height)

	def expand(self, times):

		"""Implementation independent Abstraction"""

		self._length = self._length * times
		self._breadth = self._breadth * times
		self._height = self._height * times


"""Instantiate a cuboid and pass to it an
object of ProducingAPIone"""

cuboid1 = Cuboid(1, 2, 3, ProducingAPI1())
cuboid1.produce()

cuboid2 = Cuboid(19, 19, 19, ProducingAPI2())
cuboid2.produce()

