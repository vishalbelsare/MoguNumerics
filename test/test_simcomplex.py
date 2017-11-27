
import unittest
import numpy as np

from mogu.topology import SimplicialComplex, AlphaComplex

# circular ring
ring = np.array([[np.cos(t), np.sin(t)] for t in np.linspace(0, 2*np.pi, 1001)])[1:]

# spherical ball
sphere = np.array([[np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)] for theta in np.linspace(0.02, np.pi, 51) for phi in np.linspace(0.02, 2*np.pi, 51)])

class test_simcomplex(unittest.TestCase):
    def setUp(self):
        self.sc1 = SimplicialComplex(simplices=[(1, 2), (2, 3), (1, 2, 3)])
        self.sc2 = AlphaComplex(ring, 0.1)
        self.sc3 = AlphaComplex(sphere, 0.1)

    def tearDown(self):
        pass

    def test_sc1(self):
        self.assertEqual(self.sc1.betti_number(0), 1)
        self.assertEqual(self.sc1.betti_number(1), 0)

    def test_sc1_sparse(self):
        self.assertEqual(self.sc1.betti_number(0, eps=0.001), 1)
        self.assertEqual(self.sc1.betti_number(1, eps=0.001), 0)

    def test_sc2(self):
        self.assertEqual(len(self.sc2.simplices), 1000)
        self.assertEqual(self.sc2.betti_number(0), 1)
        self.assertEqual(self.sc2.betti_number(1), 1)
        self.assertEqual(self.sc2.betti_number(2), 0)

    def test_sc2_sparse(self):
        self.assertEqual(len(self.sc2.simplices), 1000)
        self.assertEqual(self.sc2.betti_number(0, eps=0.001), 1)
        self.assertEqual(self.sc2.betti_number(1, eps=0.001), 1)
        self.assertEqual(self.sc2.betti_number(2, eps=0.001), 0)

    def test_sc3(self):
        self.assertEqual(len(self.sc3.simplices), 5195)
        self.assertEqual(self.sc3.betti_number(0), 51)
        self.assertEqual(self.sc3.betti_number(1), 0)
        self.assertEqual(self.sc3.betti_number(2), 1)
        self.assertEqual(self.sc3.betti_number(3), 0)

    def test_sc3_sparse(self):
        self.assertEqual(len(self.sc3.simplices), 5195)
        self.assertEqual(self.sc3.betti_number(0, eps=0.001), 51)
        self.assertEqual(self.sc3.betti_number(1, eps=0.001), 0)
        self.assertEqual(self.sc3.betti_number(2, eps=0.001), 1)
        self.assertEqual(self.sc3.betti_number(3, eps=0.001), 0)


if __name__ == '__main__':
    unittest.main()