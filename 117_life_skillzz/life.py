#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Optional

import numpy as np
import unittest


class LifeSimulation(object):
    def __init__(self, start_field: Optional[np.ndarray] = None):
        self.populations_number = []
        default_field = np.array([[0,1,1],
                                  [1,1,0],
                                  [0,1,0]])
        self.field = default_field if start_field is None else start_field

    def _simulate_one_step(self):
        pass

    def get_field(self) -> np.ndarray:
        return self.field

    def get_population_num(self) -> int:
        return 5

    def simulate_life(self, iterations: int):
        iters = iterations
        while iters:
            self._simulate_one_step()
            iters -= 1


class LifeSimulationTest(unittest.TestCase):
    def test_population_num_on_start(self):
        sim = LifeSimulation()
        self.assertEqual(sim.get_population_num(), 5)

    def test_user_can_set_custom_field(self):
        my_field = np.array([[0,1],[1,0]])
        sim = LifeSimulation(my_field)
        np.testing.assert_array_equal(sim.get_field(), my_field)

if __name__ == '__main__':
    unittest.main()
