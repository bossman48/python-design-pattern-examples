"""
Composite Method is a Structural Design Pattern which describes a group of objects that is treated the same way as a single instance of the same type of the objects. The purpose of the Composite Method is to Compose objects into Tree type structures to represent the whole-partial hierarchies.

One of the main advantages of using the Composite Method is that first, it allows you to compose the objects into the Tree Structure and then work with these structures as an individual object or an entity.
"""
"""
Advantages

Open/Closed Principle: As the introduction of new elements, classes and interfaces is allowed into the application without breaking the existing code of the client, it definitely follows the Open/Closed Principle
Less Memory Consumption: Here we have to create less number of objects as compared to the ordinary method, which surely reduces the memory usage and also manages to keep us away from errors related to memory
Improved Execution Time: Creating an object in Python doesn’t take much time but still we can reduce the execution time of our program by sharing objects.
Flexibility: It provides flexibility of structure with manageable class or interface as it defines class hierarchies that contains primitive and complex objects.

Disadvantages

Restriction on the Components: Composite Method makes it harder to restrict the type of components of a composite. It is not preferred to use when you don’t want to represent a full or partial hierarchy of the objects.
General Tree Structure: The Composite Method will produce the overall general tree, once the structure of the tree is defined.
Type-System of Language: As it is not allowed to use the type-system of the programming language, our program must depend on the run-time checks to apply the constraints.

Applicability

Requirement of Nested Tree Structure: It is highly preferred to use Composite Method when you are need of producing the nested structure of tree which again include the leaves objects and other object containers.
Graphics Editor: We can define a shape into types either it is simple for ex – a straight line or complex for ex – a rectangle. Since all the shapes have many common operations, such as rendering the shape to screen so composite pattern can be used to enable the program to deal with all shapes uniformly.


"""

"""Here we attempt to make an organizational hierarchy with sub-organization,
which may have subsequent sub-organizations, such as:
GeneralManager								 [Composite]
	Manager1								 [Composite]
			Developer11					 [Leaf]
			Developer12					 [Leaf]
	Manager2								 [Composite]
			Developer21					 [Leaf]
			Developer22					 [Leaf]"""

class LeafElement:

	'''Class representing objects at the bottom or Leaf of the hierarchy tree.'''

	def __init__(self, *args):

		''''Takes the first positional argument and assigns to member variable "position".'''
		self.position = args[0]

	def showDetails(self):

		'''Prints the position of the child element.'''
		print("\t", end ="")
		print(self.position)


class CompositeElement:

	'''Class representing objects at any level of the hierarchy
	tree except for the bottom or leaf level. Maintains the child
	objects by adding and removing them from the tree structure.'''

	def __init__(self, *args):

		'''Takes the first positional argument and assigns to member
		variable "position". Initializes a list of children elements.'''
		self.position = args[0]
		self.children = []

	def add(self, child):

		'''Adds the supplied child element to the list of children
		elements "children".'''
		self.children.append(child)

	def remove(self, child):

		'''Removes the supplied child element from the list of
		children elements "children".'''
		self.children.remove(child)

	def showDetails(self):

		'''Prints the details of the component element first. Then,
		iterates over each of its children, prints their details by
		calling their showDetails() method.'''
		print(self.position)
		for child in self.children:
			print("\t", end ="")
			child.showDetails()


"""main method"""

if __name__ == "__main__":

	topLevelMenu = CompositeElement("GeneralManager")
	subMenuItem1 = CompositeElement("Manager1")
	subMenuItem2 = CompositeElement("Manager2")
	subMenuItem11 = LeafElement("Developer11")
	subMenuItem12 = LeafElement("Developer12")
	subMenuItem21 = LeafElement("Developer21")
	subMenuItem22 = LeafElement("Developer22")
	subMenuItem1.add(subMenuItem11)
	subMenuItem1.add(subMenuItem12)
	subMenuItem2.add(subMenuItem22)
	subMenuItem2.add(subMenuItem22)

	topLevelMenu.add(subMenuItem1)
	topLevelMenu.add(subMenuItem2)
	topLevelMenu.showDetails()

