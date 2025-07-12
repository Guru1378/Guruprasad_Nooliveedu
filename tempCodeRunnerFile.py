class Calculator:
    
    def operate(self, operation,a,b):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Cannot divide by zero"
        else:
            return "Enter valid operation"
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

operation = input("Enter operation (add, subtract, multiply, divide): ")
result = obj.operate(operation,a,b)
print(result)