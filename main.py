import math


def sqrt(num):
    print(math.sqrt(num))


if __name__ == '__main__':

    # Basic Data Types
    x = 10  # integer
    y = 3.14  # float
    z = "Hello, World!"  # string
    print(x, y, z)

    # Built-in Data Structures
    my_list = [1, 2, 3, "Python", True]  # list
    my_tuple = (10, 20, 30)  # tuple
    my_dict = {"name": "John", "age": 25}  # dictionary
    my_set = {1, 2, 2, 3, 3, 3}  # set
    print(my_list, my_tuple, my_dict, my_set)

    # If-Else
    age = 20
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
    # For Loop
    for i in range(5):
        print(i)

    # Call Function
    sqrt(16)

    # Loops
    myList = [1, 2, 3, 4, 5]
    for i in myList:
        print(i)

    # List Comprehension
    squares = [x ** 2 for x in myList]
    print(squares)

    # Indentation
