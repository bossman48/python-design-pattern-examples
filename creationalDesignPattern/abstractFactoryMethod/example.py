# Python Code for object
# oriented concepts using
# the abstract factory
# design pattern

"""
Its solution is to replace the straightforward object construction calls with calls to the special abstract factory method. 
Actually, there will be no difference in the object creation but they are being called within the factory method. 
Now we will create a unique class whose name is Course_At_GFG which will handle all the object instantiation automatically. 
Now, we don’t have to worry about how many courses we are adding after some time.
"""


"""
Advantages of using Abstract Factory method:

This pattern is particularly useful when the client doesn’t know exactly what type to create. 

It is easy to introduce new variants of the products without breaking the existing client code.
Products which we are getting from the factory are surely compatible with each other.

Disadvantages of using Abstract Factory method:

Our simple code may become complicated due to the existence of a lot of classes.
We end up with a huge number of small files i.e, cluttering of files.

Applicability:

Most commonly, abstract factory method pattern is found in the sheet metal stamping equipment used in the manufacture of automobiles.
It can be used in a system that has to process reports of different categories such as reports related to input, output, and intermediate transactions.
"""

import random


class Course_At_GFG:

	""" GeeksforGeeks portal for courses """

	def __init__(self, courses_factory=None):
		"""course factory is out abstract factory"""

		self.course_factory = courses_factory

	def show_course(self):
		"""creates and shows courses using the abstract factory"""

		course = self.course_factory()

		print(f'We have a course named {course}')
		print(f'its price is {course.Fee()}')


class DSA:

	"""Class for Data Structure and Algorithms"""

	def Fee(self):
		return 11000

	def __str__(self):
		return "DSA"


class STL:

	"""Class for Standard Template Library"""

	def Fee(self):
		return 8000

	def __str__(self):
		return "STL"


class SDE:

	"""Class for Software Development Engineer"""

	def Fee(self):
		return 15000

	def __str__(self):
		return 'SDE'


def random_course():
	"""A random class for choosing the course"""
	return random.choice([SDE, STL, DSA])()


if __name__ == "__main__":
    course = Course_At_GFG(random_course)
    print("Course: ",course.course_factory.__doc__)
    for i in range(5):
        print("Random choice: ",random_course())
        course.show_course()

"""
no design patterns
# main method
if __name__ == "__main__":
 
    sde = SDE()    # object for SDE class
    dsa = DSA()    # object for DSA class
    stl = STL()    # object for STL class
 
    print(f'Name of the course is {sde} and its price is {sde.price()}')
    print(f'Name of the course is {dsa} and its price is {dsa.price()}')
    print(f'Name of the course is {stl} and its price is {stl.price()}')
"""