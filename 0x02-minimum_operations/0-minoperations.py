#!/usr/bin/python3
""" computes a minimum operations """


def minOperations(n):
    """
    compute the minimum number

    Args:
        n: input value
        factor_list: List to save the operations
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    fct_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                fct_list.append(i)
    return sum(fct_list)
