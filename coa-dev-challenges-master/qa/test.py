import pytest
from validate_url import *

# Demonstrate how the use pytest
def example_func(x):
    return x + 1

def test_example_failure():
    assert example_func(4) == 5

def test_example_success():
    assert example_func(1) == 2

# Example with our function
def test_identity():
    assert validate_url("www.austintexas.gov") == "www.austintexas.gov"

# Write your own tests below
# The names of your functions must be prefixed with "test_" in order for pytest to pick them up.

def test_validURL_withAll3ValidationRule_0():
    assert validate_url("www.austintexas.com?a=1&b=2&b=2',['b']") == "www.austintexas.gov?a=1&b=2"

def test_validURL_positiveVerify_1():
    assert validate_url("www.austintexas.gov?a=1&b=2&b=2") == "www.austintexas.gov?a=1&b=2"

#This test case fails due to invalid URL 
def test_validURL_withANDkeyword_2():
    assert validate_url("www.austintexas.gov?a=1&b=2andb=2") == "www.austintexas.gov?a=1&b=2"

#This test case fails due to invalid URL 
def test_validURL_withParamValueAnd2Equals_3():
   assert validate_url("www.austintexas.gov?a==1&b=2") == "www.austintexas.gov?a=1&b=2"
	
def test_validURL_noFirstParamValue_4():
   assert validate_url("www.austintexas.gov?a=&b=6") == "www.austintexas.gov?b=6"
   
def test_validURL_missingSecondParam_5():
   assert validate_url("www.austintexas.gov?a=1&") == "www.austintexas.gov?a=1"	

#This test case fails due to invalid URL 
def test_invalidURL_6():
   assert validate_url("ww.austintexas.gov?a=1") == "www.austintexas.gov?a=1"	
   
def test_validURL_positiveVerify_withSpecialChar_7():
    assert validate_url("www.austintexas.com?") == "www.austintexas.gov"

#This test case fails due to invalid URL 
def test_VerifyInvalidURL_8():
    assert validate_url("www.austintexas,com") == "www.austintexas.gov"	

#This test case fails the URL validator Rule 2 and gives error
def test_2ndValidArgument_9():
    assert validate_url("www.austintexas.gov?a=1&b=2', ['b']") == "www.austintexas.gov?a=1"

#This test case passes but the validation is not as per the URL validator Rule 2
def test_2ndInValidArgument_10():
    assert validate_url("www.austintexas.gov?a=1&b=2', ['b']") == "www.austintexas.gov?a=1&b=2"

def test_ParamValueCharEqualsChar_11():
    assert validate_url("www.austintexas.gov?a=1&b=b") == "www.austintexas.gov?a=1&b=b"
	
def test_MissingValue2ndArgument_12():
    assert validate_url("www.austintexas.gov?a=1&b=', [b]") == "www.austintexas.gov?a=1"

def test_Empty2ndArgument_13():
    assert validate_url("www.austintexas.gov?a=1&b=1', []") == "www.austintexas.gov?a=1&b=1"
	
def test_Empty2ndArgument_13():
    assert validate_url("www.austintexas.gov?a=1&b=1', []") == "www.austintexas.gov?a=1&b=1"
	
def test_ArgumentwithmissingString_14():
    assert validate_url("www.austintexas.gov?a=1&b=1', [b]") == "www.austintexas.gov?a=1&b=1"