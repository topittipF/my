def find_smallest_number():
    # Prompt the user to input three numbers
    num1 = float(input("1 "))
    num2 = float(input("10 "))
    num3 = float(input("200 "))

    # Finding the smallest number
    smallest = num1
    if num2 < smallest:
        smallest = num2
    if num3 < smallest:
        smallest = num3

    # Print the smallest number
    print("The smallest number is:", smallest)