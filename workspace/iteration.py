# Loops in Python

# Iteration using for loop
def forloop(number):
    for i in range(1,number +1):
        print(i)

forloop(15)

# Iteration using while loop
def whileloop(number):
    i=0
    while(i<number+1):
        print(i)
        i=i+1
whileloop(10)

# Foreach type statement in python
names=("saurav", "aradhana", "samarpan")
def forloopArray():
       for n in names:
           papa = "saurav"
           if(n == papa):
               print("papa of the house is:", n)

if __name__=="__main__":
    forloopArray()

# Break statements in Python
def breakstatement():
    for i in range(5,10):
        if(i ==7): break
        print(i)
if __name__ == "__main__":
    breakstatement()

# Continue statements in Python
def continueStatement():
    for i in range(5,10):
        if(i ==7): continue
        print(i)
if __name__ == "__main__":
    continueStatement()

Example 2: Continue

def continueEx2():
    for i in range(1,10):
        if(i % 2 == 0 ): continue
        print(i)

if __name__=="__main__":
    continueEx2()

Finding index of array

def indexFinder():
    names="saurav", "aradhana", "arul"
    for i,d in enumerate(names):
        print(i,d)

if __name__ == "__main__":
    indexFinder()

