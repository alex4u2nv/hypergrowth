import hashlib
import unittest
import uuid

import pytest

from hypergrowth.framework import Component, Qualifier


class MyComp(Component):

    def __init__(self, *args, **kwargs):
        self._internal = str(uuid.uuid4().hex)

    def internal(self):
        return self._internal


class TestFramework(unittest.TestCase):

    def test_component(self):
        a = MyComp()
        b = MyComp()
        self.assertNotEqual(a, b)
        self.assertNotEqual(a.internal(), b.internal())
        self.assertEqual(MyComp.instance(), MyComp.instance())
        self.assertEqual(MyComp.instance().instance, MyComp.instance().instance)

    def test_get_md5(self):
        name = "testing"
        qual = Qualifier(name=name)
        md5 = hashlib.md5()
        md5.update(name.encode("UTF-8"))
        assert md5.hexdigest().lower() == qual.get_md5()
