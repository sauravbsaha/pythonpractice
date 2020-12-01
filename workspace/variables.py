# Declaring the variables
# Python is very smart. It does not need any declaration. It figures it out by its own

# Integer variable declaration
a=10
b=2

# Addition and output
c=a+b
print(c)

# String value declaration
a="Array"
print(a[1])

# Local and Global variables
def globtest():
    a="I am a local variable inside a funcation."
    print(a)
globtest()

print("global a function:", a)