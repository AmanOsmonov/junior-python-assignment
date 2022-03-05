from django.test import TestCase
from .analiz import *


class Test_i(TestCase):

    def test_kolSogGlas(self):
        t = 'sdfghsdfg'
        r=kolSogGlas(t)
        self.assertEqual(r)

    def test_kolPov(self):
        t = 'sdfghsdfg'
        r = kolPov(t)
        self.assertEqual(r)

    def test_dslov(self):
        t = 'sdfghsdfg'
        r =dlslov(t)
        self.assertEqual(r)

    def test_srdlina(self):
        t = 'sdfghsdfg'
        r = srdlina(t)
        self.assertEqual(r)

    def test_kolB(self):
        t = 'sdfghsdfg'
        r = kolB(t)
        self.assertEqual(r)

# Create your tests here.
