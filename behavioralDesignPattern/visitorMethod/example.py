"""

Visitor Method is a Behavioral Design Pattern which allows us to separate the algorithm from an object structure on which it operates. It helps us to add new features to an existing class hierarchy dynamically without changing it. All the behavioral patterns proved as the best methods to handle the communication between the objects. Similarly, it is used when we have to perform an operation on a group of similar kinds of objects.
A Visitor Method consists of two parts: 

method named as Visit() implemented by the visitor and used and called for every element of the data structure.
Visitable classes providing Accept() methods that accept a visitor

"""


"""

Advantages

Open/Closed principle: Introducing new behavior in class is easy which can work with objects of different classes without making changes in these classes.
Single Responsibility Principle: Multiple versions of same behavior can be operated into the same class.
Addition of entities: Adding an entity in Visitor Method is easy as we have to make changes in visitor class only and it will not affect the existing item.
Updating Logic: If the logic of operation is updated, then we need to make change only in the visitor implementation rather than doing it in all the item classes.

Disadvantages

Lots of Updates: We have to update each and every visitor whenever a class get added or removed form the primary hierarchy
Hard to Extend: If there are too many visitor classes then it becomes really hard to extend the whole interface of the class.
Lack of Access: Sometimes visitors might not have the access to private field of certain classes that they are supposed to work with.

Applicability 

Recursive structures: Visitor Method works really well with recursive structures like directory trees or XML structures. The Visitor object can visit each node in the recursive structure
Performing Operations: We cam use the visitor method when we have to perform operations on all the elements of the complex object like Tree.


"""

""" The Courses hierarchy cannot be changed to add new
functionality dynamically. Abstract Crop class for
Concrete Courses_At_GFG classes: methods defined in this class
will be inherited by all Concrete Courses_At_GFG classes."""

class Courses_At_GFG:

	def accept(self, visitor):
		visitor.visit(self)

	def teaching(self, visitor):
		print(self, "Taught by ", visitor)

	def studying(self, visitor):
		print(self, "studied by ", visitor)


	def __str__(self):
		return self.__class__.__name__


"""Concrete Courses_At_GFG class: Classes being visited."""
class SDE(Courses_At_GFG): pass

class STL(Courses_At_GFG): pass

class DSA(Courses_At_GFG): pass


""" Abstract Visitor class for Concrete Visitor classes:
method defined in this class will be inherited by all
Concrete Visitor classes."""
class Visitor:

	def __str__(self):
		return self.__class__.__name__


""" Concrete Visitors: Classes visiting Concrete Course objects.
These classes have a visit() method which is called by the
accept() method of the Concrete Course_At_GFG classes."""
class Instructor(Visitor):
	def visit(self, crop):
		crop.teaching(self)


class Student(Visitor):
	def visit(self, crop):
		crop.studying(self)


"""creating objects for concrete classes"""
sde = SDE()
stl = STL()
dsa = DSA()

"""Creating Visitors"""
instructor = Instructor()
student = Student()

"""Visitors visiting courses"""
sde.accept(instructor)
sde.accept(student)

stl.accept(instructor)
stl.accept(student)

dsa.accept(instructor)
dsa.accept(student)

