#!/usr/bin/python3
<<<<<<< HEAD

=======
>>>>>>> bef071bb49a026192ca1497aaffdbc0ed6c3453f
import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().
<<<<<<< HEAD
    If a ValueError message is caught, a corresponding
    message is printed to standard error.
    Args:
        value (int): The integer to print.
=======

    If a ValueError message is caught, a corresponding
    message is printed to standard error.
    
    Args:
        value (int): The integer to print.
    
>>>>>>> bef071bb49a026192ca1497aaffdbc0ed6c3453f
    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
