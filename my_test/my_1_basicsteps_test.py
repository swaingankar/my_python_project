import pytest

def test_success():
    """this test succeeds"""
    assert True

def test_new_success():
    """this test succeeds"""
    assert True

def test_new_success_1():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')

def test_skip_1():
    """this test is skipped"""
    pytest.skip('without a reason!')

def test_broken():
    raise TypeError('pia is great , oops again')

