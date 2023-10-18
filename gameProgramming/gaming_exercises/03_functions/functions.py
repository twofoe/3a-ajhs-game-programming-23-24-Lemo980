#Functions 10/18/23, Eliot Blanton

def functionName(): #Function signature
    print("What is your name?")
    name = input("Please type your name then press enter.\n")
    print(f"Hello, {name}. \n")
    
#Call the function
functionName()

def happyBirthday(numTimes, age):
    count = 0
    while count < numTimes:
        print("Happy birthday\n")
        count += 1
    print(f"Wow you're {age} years old!\n")
    

#happyBirthday(5, 16)

def functionWithReturn(num1, num2):
    sum = num1+ num2
    quotient = sum / 5
    return quotient #return immediately exits a function

def functionWithoutReturn(num1, num2):
    sum = num1+ num2
    quotient = sum / 5

example = functionWithoutReturn(5,10)
print(example)