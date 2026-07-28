# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def fbs(n):
    if n <= 0:
        print("Invalid input, try again.")
    else:
        arrangement=[]
        a = 0
        b = 1
        for i in range(n):
                arrangement.append(a)
                a = b
                b = a+b
    print("Fibonacci sequence: ", " ".join(map(str,arrangement)))
            
def cfbs(number):
        if number<0:
               print("try again.")
               return False
        
        a=0
        b=1
        while a < number:
                a=b
                b=a+b    
                if a == number:
                    return True
                else:
                    return False
        
           
try:        
    Number=int(input("How many terms? \n"))
    fbs(Number)
    print  ("fibonacci sequence of first", Number,"terms")
except ValueError:
    print  ("try again.")

print(" "*40)
try:
    CFB=int(input("Enter number: "))
    if cfbs(CFB):
        print(CFB, "is a fibonacci number.")
    else:
        print(CFB, "is NOT a fibonacci number.")
except ValueError:
     print("try again.")
        






        
              