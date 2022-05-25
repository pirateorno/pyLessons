class python():
    def printText(a):
        print(a)

class module_helloWorld(python):
    python.printText("Hello world")

class module_1Plus1(python, module_helloWorld):
    python.printText("1+1")

a = python
b = module_helloWorld
c = module_1Plus1
