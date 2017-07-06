#! /usr/bin/env/python

import unittest
from vector import Vector

p=Vector()
v=Vector().NewCoords([1,3])
w=Vector([2,2,1])
q=Vector().NewCoords([2,2,1])
r=Vector()

class Tests(unittest.TestCase):
    def testaCoords(self):
        assert p.coords == [0,0,0]
        assert v.coords == [1,3]
        assert w.coords == [2,2,1]
        assert q.coords == [2,2,1]
    def testbDim(self):
        assert p.dim == 3
        assert v.dim == 2
        assert w.dim == 3
    def testcLength(self):
        assert p.length() == 0
        assert v.length() == (1**2 + 3**2)**0.5
        assert w.length() == (2**2 + 2**2 + 1**2)**0.5
    def testdEquals(self):
        assert q == w
        assert p == r
        assert w != v
        assert p != v
    def testeAdd(self):
        v=Vector().NewCoords([1,2,3])
        assert v == p + v
        assert w == p + w
        assert v + w == [3,4,4]
    def testfSub(self):
        v=Vector().NewCoords([1,2,3])
        assert -v == p - v
        assert p == v - v
        assert r == q - w
        assert w - v == [1,0,-2]
    def testgMul(self):
        v=Vector().NewCoords([1,2,3])
        assert p == v*0
        assert w*p == 0
        assert v*w == 9
        assert v*w == w*q
        
if __name__ == '__main__':
    unittest.main()

