import fractions as fra
import math
import unittest

def nww(a, b):
    return a*b//math.gcd(a, b)

def add_frac(frac1, frac2):
    if frac1[1] == 0 or frac2[1] == 0:
        return "Operacja niedozwolona, nie wolno dzielić przez zero"
    mianownik = nww(frac1[1],frac2[1])
    x = mianownik / frac1[1]
    y = mianownik / frac2[1]
    result = []
    result.append(frac1[0]*x + frac2[0]*y)
    result.append(mianownik)
    return result

def sub_frac(frac1, frac2):
    if frac1[1] == 0 or frac2[1] == 0:
        return "Operacja niedozwolona, nie wolno dzielić przez zero"
    mianownik = nww(frac1[1], frac2[1])
    x = mianownik / frac1[1]
    y = mianownik / frac2[1]
    result = []
    result.append(frac1[0] * x - frac2[0] * y)
    result.append(mianownik)
    return result

def mul_frac(frac1, frac2):
    if frac1[1] == 0 or frac2[1] == 0:
        return "Operacja niedozwolona, nie wolno dzielić przez zero"
    result = []
    result.append(frac1[0]*frac2[0])
    result.append(frac1[1]*frac2[1])
    return result
def div_frac(frac1, frac2):
    if frac1[1] == 0 or frac2[1] == 0:
        return "Operacja niedozwolona, nie wolno dzielić przez zero"
    result = []
    result.append(frac1[0]*frac2[1])
    result.append(frac1[1]*frac2[0])
    return result


def is_positive(frac):
    if frac[1] == 0:
        return "Operacja niedozwolona, nie wolno dzielić przez zero"
    if (frac[0]>0 and frac[1]>0) or (frac[0]<0 and frac[1]<0):
        return True
    else:
        return False

def is_zero(frac):
    if frac[1] == 0:
        return "Operacja niedozwolona, nie wolno dzielić przez zero"
    if frac[0]==0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):
    mianownik = nww(frac1[1], frac2[1])
    x = mianownik / frac1[1]
    y = mianownik / frac2[1]
    if frac1[0]*x > frac2[0]*y:
        return -1
    elif frac1[0]*x == frac2[0]*y:
        return 0
    else: return 1

def frac2float(frac):
    if frac[1] == 0:
        return "Operacja niedozwolona, nie wolno dzielić przez zero"
    result = frac[0]/frac[1]
    return result


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3,2])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([1, 2]),False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([3,4],[2,3]),-1)

    def test_frac2float(self):
        self.assertEqual(frac2float([2,5]),0.4)



if __name__ == '__main__':
    unittest.main()