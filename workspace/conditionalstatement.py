# Conditional statements

def comparisonOperator(number1, number2):
    if(number2 > number1):
        st= "Second number is greater than First number"
    #elif can also be used as else if statements
    else:
        st= "First number is larger than second one"
    print(st)

if __name__=="__main__":
    comparisonOperator(13,4)

# One liner
def comparisonOperatorOneliner(number1, number2):
    st= "Second number is greater than First number" if(number2 > number1) else "First number is larger than second one"
    print(st)

if __name__=="__main__":
    comparisonOperatorOneliner(13,4)
