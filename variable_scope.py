# a exercise messing around with local, enclosed, and global variable scoping.
# https://www.smallsurething.com/how-variable-scope-works-in-python/
x = "I am a global variable, x."

# looks for x locally in the function, doesn't find it, so it looks globally and finds it at line 1
def global_print():
	#global x
	print("I am going to print the global variable....")
	print(x)

# Defines a local variable, looks for x finds it locally and prints it.
def local_print():
	x = "I am a local variable, x."
	print("I am going to print the local variable....")
	print(x)

# specifies that x in the function refers to GLOBAL variable x. Sets GLOBAL variable x to a new string and prints
def global_redefine_print():
	global x
	x = "I am a redefined global variable"
	print(x)

def local_enclosing():
	x = "I am enclosed variable the FIRST."
	def inception():
		x = "I am a local, enclosed variable SECOND."
		print(x)		
	inception()
	print(x)		


global_print()
local_print()
global_redefine_print()
# you can see that the output of the function below changes the second time because the global variable was changed.
global_print()
# despite there being no local definition in inception there IS a local definition of x in the outer function. The enclosing variable IS local so we don't use a global variable for x.
local_enclosing()
