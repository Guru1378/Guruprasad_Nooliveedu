class Calculator:
    
    def operate(self, operation,a,b):
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b != 0:
                return a / b
            else:
                return "Cannot divide by zero"
        else:
            return "Enter valid operation"
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
obj= Calculator()
operation = input("Enter operation (add, subtract, multiply, divide): ")
result = obj.operate(operation,a,b)
print(result)