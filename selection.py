def getHello():
	return "Hello"

def getWorld():
	return "World"

def getHelloWorld():
	return f"{getHello()} {getWorld()}!"

def functionWithParam(param1, param2):
	return f"{param1 = }, {param2 = }"

def printOptions():
	print("[1] getHello()")
	print("[2] getWorld()")
	print("[3] getHelloWorld()")
	print("[4] functionWithParam(param1, param2)")



def main():
	running = True

	while running:
		printOptions()
		eingabe = input("Choose function > ")
		if eingabe == "1":
			print(getHello())
		elif eingabe == "2":
			print(getWorld())
		elif eingabe == "3":
			print(getHelloWorld())
		elif eingabe == "4":
			params = input("Type in parameters seperated by ; > ")
			if ";" in params:
				print(functionWithParam(params.split(";")[0], params.split(";")[1]))
		elif eingabe == "exit":
			running = False
		else:
			print(f"'{eingabe}': command not found\nLeave program with exit or choose a valid option:")

if __name__ == '__main__':
	main()
