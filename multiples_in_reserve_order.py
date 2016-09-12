# Design an efficient program that prints out, in reverse order, every multiple
# of 7 that is between 1 and 300. Extend the program to other multiples and number 
# ranges. Write the program in any programming language of your choice.

def number():
    multiple_number = int(raw_input("Enter the Multiple Number: "))
    start_range = int(raw_input("Enter the Start Range Number: "))
    end_range = int(raw_input("Enter the End Range Number: "))
    for i in range(start_range, end_range+1) [::-1]:
        if i % multiple_number == 0:
            print i,

number()