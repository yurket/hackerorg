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
        self.field = default_field if start_field is None else np.array(start_field)
        assert self.field.ndim == 2, f'Field should be 2 dimentional, not {self.field.ndim}-dimentional! E.g. [[1]], [[0,0,1],[0,1,1],[1,0,0]]'

    def _expand_field_if_needed(self):
        first_row = self.field[0,:]
        if np.sum(first_row == 1):
            self.field = np.vstack((np.zeros_like(first_row), self.field))

        last_row = self.field[-1,:]
        if np.sum(last_row == 1):
            self.field = np.vstack((self.field, np.zeros_like(last_row)))

        left_col = self.field[:, [0]]
        if np.sum(left_col == 1):
            self.field = np.hstack((np.zeros_like(left_col), self.field))

        right_col = self.field[:, [-1]]
        if np.sum(right_col == 1):
            self.field = np.hstack((self.field, np.zeros_like(right_col)))


    def _simulate_one_step(self):
        self._expand_field_if_needed()

    def get_field(self) -> np.ndarray:
        return self.field

    def get_population_num(self) -> int:
        return np.sum(self.field == 1)

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

    def test_exand_field_doesnt_expand_zero_field(self):
        zero_field = [[0]]
        sim = LifeSimulation(zero_field)
        sim._expand_field_if_needed()

        np.testing.assert_array_equal(sim.get_field(), zero_field)

    def test_exand_field_expands_one_field(self):
        ones_field = np.array([[1]])
        sim = LifeSimulation(ones_field)
        sim._expand_field_if_needed()

        expanded = np.array([[0,0,0],
                             [0,1,0],
                             [0,0,0]])
        np.testing.assert_array_equal(sim.get_field(), expanded)



if __name__ == '__main__':
    unittest.main()
