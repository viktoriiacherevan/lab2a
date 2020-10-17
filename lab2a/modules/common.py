import datetime
import sys
import logging

def show_numbers(pair):
    i = 0
    while i < 101:
        if i % 2 == 0 and pair:
            print(i)
        elif i % 2 != 0 and not pair:
            print(i)
        i += 1

def get_factorial(number):
    try:
        i = 1
        factorial = 1
        while i <= number:
            factorial *= i
            i += 1
        logging.info(factorial)
    except Exception as e:
        logging.warning(e)


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform