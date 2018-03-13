#!/usr/bin/python2
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import unittest
from message import *


class TestsCaesar(unittest.TestCase):

    def test(self):
        self.assertEqual(encrypt('Some string to test...', 'cezar', 7), 'Zvtl zaypun av alza...')
        self.assertEqual(decrypt('Nq Znvberz Qrv Tybevnz!', 'cezar', 13), 'Ad Maiorem Dei Gloriam!')
        self.assertEqual(encrypt(decrypt('Karuzela!', 'cezar', 13), 'cezar', 13), 'Karuzela!')
        self.assertEqual(encrypt('Some string to test...', 'cezar', 33), 'Zvtl zaypun av alza...')


class TestsXOR(unittest.TestCase):

    def test(self):
        self.assertEqual(encrypt('Some string to test...', 'xor', 209), '\x82\xbe\xbc\xb4\xf1\xa2\xa5\xa3\xb8\xbf\xb6\xf1\xa5\xbe\xf1\xa5\xb4\xa2\xa5\xff\xff\xff')
        self.assertEqual(decrypt('\x90\xb5\xf1\x9c\xb0\xb8\xbe\xa3\xb4\xbc\xf1\x95\xb4\xb8\xf1\x96\xbd\xbe\xa3\xb8\xb0\xbc\xf0', 'xor', 209), 'Ad Maiorem Dei Gloriam!')
        self.assertEqual(encrypt(decrypt('Karuzela!', 'xor', 298), 'xor', 298), 'Karuzela!')


if __name__ == '__main__':
    unittest.main()
