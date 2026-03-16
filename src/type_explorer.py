## int — whole numbers
# print(5)                                ## 5
# print(-12)                              ## -12
# print(0)                                ## 0
# print(type(5))                          ## class 'int'

#### Edge cases
# print(999999999999999999999999999999)   # very large int
# print(-0)                               # still 0
# print(type(-0))                         # <class 'int'>

### Conclusions
### Python integers can be very large.
###-0 becomes 0.

#===========================================================#

## float — decimal numbers
# print(3.14)                              # 3.14
# print(-0.5)                              # -0.5 
# print(0.0)                               # 0.0
# print(type(3.14))                        # <class 'float'>

#### Edge cases                            
# print(1.0)                               # 1.0
# print(.5)                                # 0.5
# print(5.)                                # 5.0
# print(0.1 + 0.2)                         # 0.30000000000000004 
# print(type(5.0))                         # <class 'float'>
# print((0.1 + 0.2) == 0.3)                # false

### Conclusions
# float precision issues
# float calculates with precision of 16x 0 and 4 after the decimal


#===========================================================#

## str - text
# print("hello")                           # hello
# print('world')                           # world
# print("")                                # empty line
# print(type("hello"))                     # <class 'str'>

#### Edge cases                            
# print("123")                             # text, not a number
# print("True")                            # text, not boolean
# print(" ")                               # one space
# print("")                                # empty string
# print(type("123"))                       # <class 'str'>

## Quotes inside strings
# print("I'm learning Python")              # I'm learning Python
# print('He said "hello"')                  # 'He said "hello"'

## Multi-line string
# print("""line 1                             
# line 2
# line 3""")

# line 1
# line 2
# line 3

## Escape characters
# print("Hello\nWorld")                    # new line
# print("Hello\tWorld")                    # tab
# print("C:\\Users\\Name")                 # C:\Users\Name

### Conclusions
# \ — Escape character
# A single backslash (\) is used to introduce escape sequences in strings.
#\n → new line
# \t → tab
# \\ → literal backslash
# \" → double quote
# \' → single quote

#===========================================================#

## bool — true/false

# print(True)                               # True
# print(False)                              # False
# print(type(True))                         # <class 'bool'>

#### Edge cases 
# print(bool(""))             # False (empty string)
# print(bool(" "))            # True (it is a value)
# print(bool("0"))            # True 
# print(bool(0))              # False 
# print(bool([]))             # False (empty array) 
# print(bool(None))           # False 

# print(True + True)                        # 2
# print(True + False)                       # 1
# print(False + False)                      # 0 

### Conclusions
# True acts like 1
# False acts like 0
# Empty container are false

# print(type(True))                         # <class 'bool'>
# print(isinstance(True, int))              # True

#===========================================================#

## NoneType — no value

# print(None)                              # None
# print(type(None))                        # <class 'NoneType'>

### Conclusion
#  Use None when something has no value yet.

#===========================================================#


## Type conversions
### Convert to int
# print(int(5.9))                          # 5 (loses numbers after decimal)
# print(int("123"))                        # 123
# print(int(True))                         # 1
# print(int(False))                        # 0 

### Edge cases
# print(int("12.5"))                       # ValueError: invalid literal for int() with base 10: '12.5'
# print(int("hello"))                      # ValueError: invalid literal for int() with base 10: 'hello' 
# print(int(None))                         # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

### Convert to float
# print(float(5))                          # 5.0
# print(float("3.14"))                     # 3.14
# print(float(True))                       # 1.0

### Edge cases
# print(float("nan"))                      # nan (not a number- a valit float)  
# print(float("inf"))                      # inf (infinity - a valit float)
# print(float("-inf"))                     # -inf (infinity - a valit float)
# print(float("hello"))                    # ValueError: could not convert string to float: 'hello'

### Convert to str

# print(str(123))                          # 123
# print(str(3.14))                         # 3.14
# print(str(True))                         # True
# print(str(None))                         # None


### Operators
# print(5 + 5)                             # 10
# print("5" + "5")                         # 55
# print(5 + "5")                           # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print(10 / 2)                            # 5.0
# print(type(10 / 2))                      # <class 'float'>
# print(10 // 2)                           # 5              
# print(7 // 2)                            # 3

## Conclusion
# Even when division is exact, / gives a float.
# Use // for floor division

