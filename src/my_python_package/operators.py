import numpy as np
def add(x, y):
    """Add two numbers or arrays.
    Parameters
    ----------
    x : int or float or array_like
    The first number to add.
    y : int or float or array_like
    The second number to add.
    Returns
    -------
    int or float or array_like
    The sum of x and y.
    """
    return x + y
def multiply(x, y):
    """Multiply two numbers or arrays.
    Parameters
    ----------
    x : int or float or array_like
    The first number to multiply.
    y : int or float or array_like
    The second number to multiply.
    Returns
    -------
    int or float or array_like
    The (element-wise) product of x and y.
    """
    return x * y

def divide(x, y):
    """"Divide two numbers or arrays.
    Parameters
    ----------
    x : int or float or array_like
    The numerator.
    y : int or float or array_like
    The denomenator.
    Returns
    -------
    int or float or array_like
    The (element-wise) quotient of x and y.
    """
    return x / y 

def exp(x, y):
    """Raise the base to the power of the exponent.
    Parameters
    ----------
    x : int or float
    The base.
    y : int or float
    The exponent.
    Returns
    -------
    int or float
    The (element-wise) power of x and y.
    """
    return x ** y