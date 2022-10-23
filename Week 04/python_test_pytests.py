""" The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries. """
import python_test_addition as addi
# python library for unite testing
import pytest


# test case 1
def test_add():
    assert True
    assert addi.add(4, 5) == 9


# test case 2
def test_sub():
    assert addi.sub(4, 5) == -1


# test case 3
def test_multi():
    # assert addi.multi(10, 0) == 0
    pass


"""
    Also we can use those functions or test them using command line like below:
    
python -m pytest python_test_pytests.py::test_sub
================================================================================= test session starts =================================================================================
platform win32 -- Python 3.9.13, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\Yash Stuff\Learning Stuff\Projects\courcera_meta_programming_in_python\Week 04
collected 1 item

python_test_pytests.py .                                                                                                                                                         [100%] 

================================================================================== 1 passed in 0.00s ================================================================================== 

"""