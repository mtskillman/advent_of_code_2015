import pytest
from day7advent import *


def test_and_gate():
    assert and_gate(60, 30) == 28

def test_or_gate():
    assert or_gate(60, 30) == 62

def test_not_gate():
    assert not_gate(526) == 65009

def test_lshift_gate_again():
    assert lshift_gate(60123, 5) == 23392

def test_lshift_gate():
    assert lshift_gate(553, 4) == 8848

def test_rshift_gate():
    assert rshift_gate(553, 3) == 69


example1 = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''

example2 = '123 -> x'



connection_table = {
    'x': 123,
    'y': 456,
    'd': ['x','and','y'],
    'e': ['x','or','y'],
    'f': ['x','lshift',2],
    'g': ['y','rshift',2],
    'h': ['not','x'],
    'i': ['not','y'],
}

sample_input = open('scratch.txt','r').readlines()


def test_parse_a_line():
    assert parse_a_line('123 -> x\n') == [123, 'x']

def test_parse_a_line_2():
    assert parse_a_line('x LSHIFT 2 -> f\n') == [['x', 'lshift', 2], 'f']

def test_parse_a_line_3():
    assert parse_a_line('NOT x -> h\n') == [['not', 'x'], 'h']

def test_parse_a_line_4():
    assert parse_a_line('1 AND cx -> cy\n') == [[1,'and','cx'], 'cy']

def test_compute_for_wire():
    assert compute_for_wire('h', connection_table) == 65412

def test_compute_for_wire_2():
    assert compute_for_wire('g', connection_table) == 114

def test_build_connection_table():
    assert build_connection_table(sample_input) == connection_table



