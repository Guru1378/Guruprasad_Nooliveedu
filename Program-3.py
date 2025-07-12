def print_odd_numbers(a):
    if a < 1:
        print("Please enter a positive integer.")
        return
    else:
        if a%2==0:
            a=a-1
        count=0
        i=1
        while True:
            print(i)
            count += 1
            if count==5:
                break
            i+=2
n = int(input("Enter a number: ")) 
print_odd_numbers(n)
