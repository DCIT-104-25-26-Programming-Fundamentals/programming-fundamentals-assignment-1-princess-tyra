# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# ============================================
# PROGRAMMING FUNDAMENTALS - Assignment 6
# Topic: Loops and Functions
# Multiplication Table Generator
# ============================================

# Function for Part A
def single_table():
    print("PART A - Single Multiplication Table")

    number = input("Enter a number: ")

    # Check if the input is a positive integer
    if not number.isdigit():
        print("Error: Please enter a positive integer.")
        return

    number = int(number)

    print("\nMultiplication Table for", number)
    print("---------------------------")

    for i in range(1, 13):
        print(number, "x", i, "=", number * i)


# Function for Part B
def tables_to_n():
    print("\nPART B - Multiplication Tables from 1 to N")

    n = input("Enter a positive integer: ")

    # Check if the input is a positive integer
    if not n.isdigit():
        print("Error: Please enter a positive integer.")
        return

    n = int(n)

    if n <= 0:
        print("Error: Please enter a positive integer greater than zero.")
        return

    for number in range(1, n + 1):
        print("\nMultiplication Table for", number)
        print("---------------------------")

        for i in range(1, 13):
            print(number, "x", i, "=", number * i)

        print("---------------------------")


# Main Program
print("WELCOME TO THE MULTIPLICATION TABLE GENERATOR")
print("=============================================")

single_table()
tables_to_n()

print("\nThank you for using the Multiplication Table Generator!")
