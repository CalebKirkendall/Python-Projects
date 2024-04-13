def calculate(num1,num2,operation):
    answer = None
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation ==  "*":
        answer = num1 * num2
    elif operation == "/":
        answer = num1 / num2
    elif operation == "**":
        answer = num1 ** num2
    elif operation == "%":
        answer = num1 % num2
    return answer

def calculation():
    print("Enter the first value:")
    x = int(input())
    print("Enter the operation you wish to do with that value:")
    op = input()
    print("Enter the second value:")
    y = int(input())
    print(calculate(x,y,op))

calculation()
print("Would you like to do another calculation? y/n")
again = input()
while again == "y":
    calculation()
    print("Another calculation? y/n")
    again = input()
print("Thanks for doing your calculations here!")