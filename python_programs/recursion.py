# function inside function & calling itself
def factorial_iterative(n):
    """
    :param n:
    :return:
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
number = int(input("enter a number:"))
res = factorial_iterative(number)
print("Factorial using iterative method",res)

def fact_recursive(n):
    if n == 1:
        return 1
    else:
        return n * fact_recursive(n-1)

x = int(input("enter a number"))
print("Using recursion",fact_recursive(x))

"""
if n = 3
in recursion:
    3 * fact_recursive(2)
    3 * 2 * fact_recursive(1)
    3 * 2 * 1 = 6

"""

