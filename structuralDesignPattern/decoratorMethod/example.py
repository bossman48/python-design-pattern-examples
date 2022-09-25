"""
Decorator Method is a Structural Design Pattern which allows you to dynamically attach new behaviors to objects without changing their implementation by placing these objects inside the wrapper objects that contains the behaviors. 
It is much easier to implement Decorator Method in Python because of its built-in feature. It is not equivalent to the Inheritance because the new feature is added only to that particular object, not to the entire subclass.

"""

"""
Advantages

 

Single Responsibility Principle: It is easy to divide a monolithic class which implements many possible variants of behavior into several classes using the Decorator method.
Runtime Responsibilities: We can easily add or remove the responsibilities from an object at runtime.
SubClassing: The decorator pattern is an alternative to subclassing. Subclassing adds behavior at compile time, and the change affects all instances of the original class; decorating can provide new behavior at runtime for individual objects.
 

Disadvantages

 

removing Wrapper: It is very hard to remove a particular wrapper from the wrappers stack.
Complicated Decorators: It can be complicated to have decorators keep track of other decorators, because to look back into multiple layers of the decorator chain starts to push the decorator pattern beyond its true intent.
Ugly Configuration: Large number of code of layers might make the configurations ugly.
 

Applicability

 

Incapable Inheritance: Generally, Decorator method is used when it is not possible to extend the behavior of an object using the Inheritance.
Runtime Assignment: One of the most important feature of Decorator method is to assign different and unique behaviors to the object at the Runtime.
"""


class WrittenText:

	"""Represents a Written text """

	def __init__(self, text):
		self._text = text

	def render(self):
		return self._text

class UnderlineWrapper(WrittenText):

	"""Wraps a tag in <u>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<u>{}</u>".format(self._wrapped.render())

class ItalicWrapper(WrittenText):

	"""Wraps a tag in <i>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<i>{}</i>".format(self._wrapped.render())

class BoldWrapper(WrittenText):

	"""Wraps a tag in <b>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<b>{}</b>".format(self._wrapped.render())

""" main method """

if __name__ == '__main__':

	before_gfg = WrittenText("GeeksforGeeks")
	after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

	print("before :", before_gfg.render())
	print("after :", after_gfg.render())

