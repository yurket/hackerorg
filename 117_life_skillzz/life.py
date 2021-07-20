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

    def _get_alive_cells_around(self, row: int, col: int) -> int:
        square_subfield = self.field[row-1:row+2, col-1:col+2]
        return np.sum(square_subfield == 1) - self.field[row, col]

    @staticmethod
    def _is_cell_alive(cell):
        return cell == 1

    def _determine_new_cell_state(self, i: int, j: int) -> int:
        n,m = self.field.shape
        assert (i-1 >= 0) and (j-1 >= 0) and (i+1 <= n) and (j+1 <= m), "Cell should not be on field edges!"
        cell = self.field[i, j]
        alive_cells_around = self._get_alive_cells_around(i, j)
        if self._is_cell_alive(cell) and (alive_cells_around == 2 or alive_cells_around == 3):
            return 1
        if not self._is_cell_alive(cell) and alive_cells_around == 3:
            return 1
        return 0

    def _simulate_one_step(self):
        self._expand_field_if_needed()

        new_field = np.zeros_like(self.field)
        n,m = self.field.shape
        for i in range(1, n-1):
            for j in range(1, m-1):
                new_field[i,j] = self._determine_new_cell_state(i, j)
        self.field = new_field

    def get_field(self) -> np.ndarray:
        return self.field

    def get_population_num(self) -> int:
        return np.sum(self.field == 1)

    def simulate_life(self, generations: int):
        iters = generations
        while iters:
            if iters and (iters % 10**5 == 0):
                print(f'{iters} generations left to simulate')
            self._simulate_one_step()
            iters -= 1


class LifeSimulationTest(unittest.TestCase):
    expanded_ones = np.array([[0,0,0],
                             [0,1,0],
                             [0,0,0]])

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

        np.testing.assert_array_equal(sim.get_field(), self.expanded_ones)

    def test_simulation_with_zero_generations_returns_original_field(self):
        sim = LifeSimulation()
        sim.simulate_life(0)

        self.assertEqual(sim.get_population_num(), 5)

    def test_counting_alive_cells_1(self):
        sim = LifeSimulation(self.expanded_ones)

        self.assertEqual(sim._get_alive_cells_around(1,1), 0)

    def test_counting_alive_cells_in_default_field(self):
        sim = LifeSimulation()
        alive_cells_around_center_cell = 4

        self.assertEqual(sim._get_alive_cells_around(1, 1), alive_cells_around_center_cell)

    def test_that_single_cell_always_dies(self):
        single_cell = [[1]]
        sim = LifeSimulation(single_cell)
        any_generations = 42
        sim.simulate_life(any_generations)

        self.assertEqual(sim.get_population_num(), 0)

    def test_solution(self):
        sim = LifeSimulation()
        ten_bils = 10*10**9
        sim.simulate_life(ten_bils)
        print(f'Population after {ten_bils} generations: {sim.get_population_num()}')


# check field shrinking

if __name__ == '__main__':
    unittest.main()
