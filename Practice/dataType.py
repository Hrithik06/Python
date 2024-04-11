x = "Hello World" # x is of type str
print(x, " = ",type(x))

x = 20 # x is now of type int
print(x, " = ",type(x))

x = 20.5 # x is now of type float
print(x, " = ",type(x))

x = 1j # x is now of type complex
print(x, " = ",type(x))

x = ["apple", "banana", "cherry"] # x is now of type list
print(x, " = ",type(x))

x = ("apple", "banana", "cherry") # x is now of type tuple
print(x, " = ",type(x))

x = range(6) # x is now of type range
print(x, " = ",type(x))

x = {"name": "John", "age": 36} # x is now of type dict
print(x, " = ",type(x))

x = {"apple", "banana", "cherry"} # x is now of type set
print(x, " = ",type(x))

x = frozenset({"apple", "banana", "cherry"}) # x is now of type frozenset
print(x, " = ",type(x))

x = True # x is now of type bool
print(x, " = ",type(x))

x = b"Hello" # x is now of type bytes
print(x, " = ",type(x))

x = bytearray(5) # x is now of type bytearray
print(x, " = ",type(x))

x = memoryview(bytes(5)) # x is now of type memoryview
print(x, " = ",type(x))

x = None # x is now of type NoneType
print(x, " = ",type(x))
