
"""
What is Singleton Method in Python
Singleton Method is a type of Creational Design pattern and is one of the simplest design patterns00 available to us. It is a way to provide one and only one object of a particular type. It involves only one class to create methods and specify the objects. 
Singleton Design Pattern can be understood by a very simple example of Database connectivity. When each object creates a unique Database Connection to the Database, it will highly affect the cost and expenses of the project. So, it is always better to make a single connection rather than making extra irrelevant connections which can be easily done by Singleton Design Pattern.

"""

"""

Advantages of using the Singleton Method: 

Initializations: An object created by the Singleton method is initialized only when it is requested for the first time.
Access to the object: We got global access to the instance of the object.
Count of instances: In singleton, method classes can’t have more than one instance
Disadvantages of using the Singleton Method: 

Multithread Environment: It’s not easy to use the singleton method in a multithread environment, because we have to take care that the multithread wouldn’t create a singleton object several times.
Single responsibility principle: As the Singleton method is solving two problems at a single time, it doesn’t follow the single responsibility principle.
Unit testing process: As they introduce the global state to the application, it makes the unit testing very hard.
Applicability

Controlling over global variables: In the projects where we specifically need strong control over the global variables, it is highly recommended to use Singleton Method
Daily Developers use: Singleton patterns are generally used in providing the logging, caching, thread pools, and configuration settings and are often used in conjunction with Factory design patterns.
"""
# Singleton Borg pattern
class Borg:

	# state shared by each instance
	__shared_state = dict()

	# constructor method
	def __init__(self):

		self.__dict__ = self.__shared_state
		self.state = 'GeeksforGeeks'

	def __str__(self):

		return self.state


# main method
if __name__ == "__main__":

	person1 = Borg() # object of class Borg
	person2 = Borg() # object of class Borg
	person3 = Borg() # object of class Borg

	person1.state = 'DataStructures' # person1 changed the state
	person2.state = 'Algorithms'	 # person2 changed the state

	print(person1) # output --> Algorithms
	print(person2) # output --> Algorithms

	person3.state = 'Geeks' # person3 changed the
	# the shared state

	print(person1) # output --> Geeks
	print(person2) # output --> Geeks
	print(person3) # output --> Geeks

