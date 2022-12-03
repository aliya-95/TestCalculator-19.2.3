import pytest


def setup():
    print("basic setup into module")


def teardown():
    print("basic teardown into module")


def setup_module(module):
    print("module setup")


def teardown_module(module):
    print("module teardown")


def setup_function(function):
    print("function setup")


def teardown_function(function):
    print("function teardown")


def test_numbers_3_4():
    print
    "test 3*4"
    assert 3 * 4 == 12

def test_numbers_3_4():
    print
    "test 3+4"
    assert 3 + 4 == 7

def test_numbers_5_1():
    print
    "test 5-1"
    assert 5 - 1 == 4

def test_numbers_5_1():
    print
    "test 10/2"
    assert 10 / 2 == 5