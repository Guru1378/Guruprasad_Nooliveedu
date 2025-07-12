def print_odd_numbers(n):
    if n < 1:
        print("Please enter a positive integer.")
        return
    else:
        for i in range (1,n+1,2):
          print(i)
n=int(input("Enter a number: "))
print_odd_numbers(n)
