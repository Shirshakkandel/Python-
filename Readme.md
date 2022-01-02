[Python Cheatsheet](https://github.com/wilfredinni/python-cheatsheet)
# 3)getting Started with python
```python
 2 ** 3 = 8 #power in python
 10 % 3= 1  # modulus in python
 print(r'c:\docs\nabin')  #r will print as it is.
```

# 4)Varibale 5)Lens 6)Tuples
```python
 name="shirshak"
 name[0] # will print s
 name[-1] #will print k
 name[0:2] #will print sh
 name[0]= "R" # will print error cause string in python is immutable(channot be change)
 len(name) #will print 8 


 #List
 nums=[25,12,36]
 nums[1:]  # will works as string
# List is mutable just like array and object in javascript

spam = ['cat', 'bat', 'rat', 'elephant']

spam = ["cat", "bat", "rat", "elephant"]
spam.sort()
print("spam list", spam)

# Tuple is immutable inside () cannot be chanage
#Set display without in sequence and support duplicate value

	Data/Variable types:
Text: String(str when writing code)
Number: Integer(int), float, complex
Sequence: list, tuple, range
Mapping: Dictionary
Boolean: bool
binary: bytes, bytearray, memoryview

	Meaning:
string: text
integer: whole number
float: decimal
complex: complex number
list: a list with multiple elements which are data types
tuple: a non editable list
range: a range of numbers
dictionary: Look in examples
boolean: True or False
byte: still working on explaination
bytearray: still working on explaination
memoryview: still working on explaination

	Examples:

Integer: x = 10
         y = 20

Float: x = 1.5
       y = 1.231

Complex: x = 1j

List: list = ["Element 1", 2, True]

Tuple: tuple = ("Element 1", 2, False)

Range: range_1 = range(1, 10)  # This will give the output of 1, 2, 3... 8, 9

Dictionary: dictionary = {"color": "red", "shape": "square"}

Boolean: boolean = True


#Still working

```


# Section 3 Operators
```python
#PYTHON RELATIONAL OPERATORS
OPERATOR    DESCRIPTION	        SYNTAX  FUNCTION        IN-PLACE METHOD
>	        Greater than	    a > b   gt(a, b)        __gt__(self, other)
>=	        Greater or equal to	a >= b  ge(a, b)        __ge__(self, other)
<	        Less than	        a < b   lt(a, b)        __lt__(self, other)
<=	        Less or equal to	a <= b  le(a, b)        __le__(self, other)
==	        Equal to	        a == b  eq(a, b)        __eq__(self, other)
!=	        Not equal to        a != b  ne(a, b)        __ne__(self, other)

#PYTHON MATHEMATICAL OPERATORS
OPERATOR	DESCRIPTION	        SYNTAX  FUNCTION        IN-PLACE METHOD
+	        Addition	        a + b   add(a, b)       __add__(self, other)
–	        Subtraction	        a - b   sub(a, b)       __sub__(self, other)
*	        Multiplication	    a * b   mul(a, b)       __mul__(self, other)
/	        True Division	    a / b   truediv(a, b)   __truediv__(self, other)
//	        Floor Division	    a // b  floordiv(a, b)  __floordiv__(self, other)
%	        Modulo	            a % b   mod(a, b)       __mod__(self, other)
**	        Power	            a ** b  pow(a, b)       __pow__(self, other)

#PYTHON BITWISE OPERATORS
OPERATOR	DESCRIPTION	        SYNTAX  FUNCTION        IN-PLACE METHOD
&	        Bitwise AND	        a & b   and_(a, b)      __and__(self, other)
|	        Bitwise OR	        a | b   or_(a,b)        __or__(self, other)
^	        Bitwise XOR	        a ^ b   xor(a, b)       __xor__(self, other)
~           Bitwise NOT         ~ a     invert(a)       __invert__(self)
>>          Bitwise R shift     a >> b  rshift(a, b)    __irshift__(self, other)
<<          Bitwise L shift     a << b  lshift(a, b)    __lshift__(self, other)

```

# Section 5 condition and loops

```python
if condition:
  	# stuff
elif condition:
  	# stuff
else:
  	# stuff
# EXEMPLE #

hour = 14

if hour < 8: # if hour is less than 8
  	print("It's morning")
elif hour < 18: # if hour is beetween 8 and 18
  	print("It's the day")
else: # if hour is upper than 18
  	print("It's the evening")


#Loop
#x starts at 1 and goes up to 80 @ intervals of 2
for x in range(1, 80, 2):
  print(x)

```

# 6)Function  
```python
def myFunction(say): #you can add variables to the function
  print(say)

myFunction("Hello")

age = input("How old are you?")

myFunction("You are {} years old!".format(age))

#this is what you get:

Hello
How old are you?
>>11 #lol my real age actually
You are 11 years old!

# numpy
arr = np.linspace(0, 15, 16)
print(arr)

# function
def add(*b):
    c = 0
    for i in b:
        c = c + i
    return c


addvalue = add(2, 4, 5, 6)
print("Added value", addvalue)  # Added value 17


def sum ( a, b ):			# non anonymous
        return a+b
print (sum(1, 2))			# 3

sum = lambda a,b: (a+b)		# anonymous / lambda
print (sum(1, 2))			# 3
```

# 7) Filter,map and reduce

```python
# Filter map and reduce

mylist = [5, 4, 6, "other random stuff", True, "22", "map", False, ""]


def multiply_by_two(obj):
    return obj * 2


def is_str(obj):
    return type(obj) == str


list(map(multiply_by_two, mylist))
# [10, 8, 12, "other random stuffother random stuff", 2, "2222", "mapmap", 0, ""]

list(filter(is_str, mylist))
# ["other random stuff", "22", "map", ""]

# You could also use lambdas on both examples:
list(map(lambda x: x * 2, mylist))
list(filter(lambda x: type(x) == str, mylist))

```