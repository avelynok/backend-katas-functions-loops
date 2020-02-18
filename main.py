#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Avelyno Koumaka"


def add(x, y):
    """Add two integers. Handles negative values."""
    add = x + y
    return add


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    product = 0
    for _ in range(0, x):
        product = add(product, y)
    return product


def power(x, n):
    """Raise x to power n, where n >= 0"""
    y = 1
    for _ in range(0, n):
        y = multiply(y, x)
    return y


def factorial(x):
    """Compute factorial of x, where x > 0"""
    y = 1
    for i in range(1, x + 1):
        y = multiply(y, i)
    return y


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    y = [0, 1]
    for i in range(2, n + 1):
        y.append(add(y[i - 2], y[i - 1]))
    return y


if __name__ == '__main__':
    # your code to call functions above
    pass
