import unittest,math
from factorial_alias_audit.core import run
class DomainTests(unittest.TestCase):
 def test_half_fraction(self):
  x=run({'factors':['A','B','C'],'runs':[[-1,-1,1],[-1,1,-1],[1,-1,-1],[1,1,1]],'max_order':2});self.assertIn(dict(left='A',right='B*C',sign=1),x['exact_aliases'])
 def test_full_factorial(self):
  import itertools
  x=run({'factors':['A','B'],'runs':[list(r)for r in itertools.product([-1,1],repeat=2)]});self.assertEqual(x['exact_aliases'],[]);self.assertEqual(x['partial_nonorthogonality'],[])
 def test_reject_nonbinary(self):
  with self.assertRaises(ValueError):run({'factors':['A'],'runs':[[0]]})
