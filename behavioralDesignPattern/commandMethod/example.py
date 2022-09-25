"""
Command Method is Behavioral Design Pattern that encapsulates a request as an object, thereby allowing for the parameterization of clients with different requests and the queuing or logging of requests. Parameterizing other objects with different requests in our analogy means that the button used to turn on the lights can later be used to turn on stereo or maybe open the garage door. It helps in promoting the “invocation of a method on an object” to full object status. Basically, it encapsulates all the information needed to perform an action or trigger an event.

"""

"""

Advantages 

Open/Closed Principle: We can introduce the new commands into the application without breaking the existing client’s code.
Single Responsibility Principle: It’s really easy to decouple the classes here that invoke operations from other classes.
Implementable UNDO/REDO: It’s possible to implement the functionalities of UNDO/REDO with the help of Command method.
Encapsulation: It helps in encapsulating all the information needed to perform an action or an event.

Disadvantages

Complexity Increases: The complexity of the code increases as we are introducing certain layers between the senders and the receivers.
Quantity of classes increases: For each individual command, the quantity of the classes increases.
Concrete Command: Every individual command is a ConcreteCommand class that increases the volume of the classes for implementation and maintenance.

Applicability 

Implementing Reversible operations: As the Command method provides the functionalities for UNDO/REDO operations, we can possibly reverse the operations.
Parameterization: It’s always preferred to use Command method when we have to parameterize the objects with the operations.
"""

"""Use built-in abc to implement Abstract classes and methods"""
from abc import ABC, abstractmethod

"""Class Dedicated to Command"""
class Command(ABC):
	
	"""constructor method"""
	def __init__(self, receiver):
		self.receiver = receiver
	
	"""process method"""
	def process(self):
		pass

"""Class dedicated to Command Implementation"""
class CommandImplementation(Command):
	
	"""constructor method"""
	def __init__(self, receiver):
		self.receiver = receiver

	"""process method"""
	def process(self):
		self.receiver.perform_action()

"""Class dedicated to Receiver"""
class Receiver:
	
	"""perform-action method"""
	def perform_action(self):
		print('Action performed in receiver.')

"""Class dedicated to Invoker"""
class Invoker:
	
	"""command method"""
	def command(self, cmd):
		self.cmd = cmd

	"""execute method"""
	def execute(self):
		self.cmd.process()

"""main method"""
if __name__ == "__main__":
	
	"""create Receiver object"""
	receiver = Receiver()
	cmd = CommandImplementation(receiver)
	invoker = Invoker()
	invoker.command(cmd)
	invoker.execute()

