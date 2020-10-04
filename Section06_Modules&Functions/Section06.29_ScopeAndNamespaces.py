__author__ = "crypto"

# Recursive function:
#                   Is a function that calls itself and they can be very useful in dealing with structures
# that contains the,selves such as directories in a computer file system.
# now for computing mathematical functions that are defined recursively.

# Lets create our factorial function "Iterative"


def fact(n):
    """ Calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


for i in range(130):
    print(i, fact(i))
# ---------------------------------------------------------------------
print('='*40)
# let's have a look about "The recursive equivalent"


def factorial(n):
    # n! can be also be defined as n * (n-1)
    """ Calculate n1 recursively"""
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)


for i in range(130):
    print(i, factorial(i))

# the difference here will be in the point where if any n is < 1 will be returned as 1
# the method works as waterful model, which mean you can't calculate fac(4) till fac(3) done
# ---------------------------------------------------------------------
print('='*40)
# Third one : Fibonacci Function


def fib(n):
    """F(n) = F(n-1) + f(n -2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n - 2)


# for i in range(36):     # why we reduce the number here? that's because Fib() takes long time to be calculates beside this's ver inefficient way to calculate Fibonacci numbers
#     #                     because Fibonacci numbers call itself twice for each number abd when it comes to Fib n - 1 it has to calculate the value for fib n-2 and re-calculate in order
#     print(i, fib(i))
# ---------------------------------------------------------------------
print('='*40)
# Let's use Fibonacci without recursive function


def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(35):
    # print(i, fib(i), fibonacci(i))
    print(i, fibonacci(i))
# ---------------------------------------------------------------------
print('='*40)
