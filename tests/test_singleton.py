import unittest
import uuid

from component.framework import Component


class MyComp(Component):

    def __init__(self, *args, **kwargs):
        self._internal = str(uuid.uuid4().hex)

    def internal(self):
        return self._internal


class TestSingleton(unittest.TestCase):

    def test_singleton(self):
        a = MyComp()
        b = MyComp()
        self.assertNotEqual(a, b)
        self.assertNotEqual(a.internal(), b.internal())
        self.assertEqual(MyComp.instance(), MyComp.instance())
        self.assertEqual(MyComp.instance().instance, MyComp.instance().instance)
