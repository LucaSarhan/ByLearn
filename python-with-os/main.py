import os
import platform

print("name of the os", os.name)
print("get the namespace", platform.system())
print("enviorment information", os.environ)
print("process id number", os.getpid())
print("the current directory", os.getcwd())
print("current file",__file__)
print("current file name", os.path.basename(__file__))
print("current file path", os.path.dirname(__file__))
print("current absolute file path", os.path.abspath(__file__))