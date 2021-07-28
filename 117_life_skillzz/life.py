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
        rows, cols = self.field.shape
        start_row = max(0, row-1)
        end_row = min(row+2, rows)
        start_col = max(0, col-1)
        end_col = min(col+2, cols)

        square_subfield = self.field[start_row:end_row, start_col:end_col]

        return np.sum(square_subfield == 1) - self.field[row, col]

    @staticmethod
    def _is_cell_alive(cell):
        return cell == 1

    def _determine_new_cell_state(self, i: int, j: int) -> int:
        n,m = self.field.shape
        assert (i >= 0) and (j >= 0) and (i <= n) and (j <= m), "Cell should not be inside the field!"
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
        for i in range(0, n):
            for j in range(0, m):
                new_field[i,j] = self._determine_new_cell_state(i, j)
        self.field = new_field
        print(f'New field size: {self.field.shape}')
        self.print_field()

    def get_field(self) -> np.ndarray:
        return self.field

    def print_field(self) -> None:
        print()
        for row in self.field:
            print('|', end='')
            for x in row:
                c = ' X ' if x else ' - '
                print(c, end='')
            print('|')

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
    def setUp(self):
        self.expanded_ones = np.array([
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ])

        self.default_sim = LifeSimulation()

    def test_population_num_on_start(self):
        self.assertEqual(self.default_sim.get_population_num(), 5)

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
        self.default_sim.simulate_life(0)

        self.assertEqual(self.default_sim.get_population_num(), 5)

    def test_counting_alive_cells_1(self):
        sim = LifeSimulation(self.expanded_ones)

        self.assertEqual(sim._get_alive_cells_around(1,1), 0)

    def test_counting_alive_cells_2(self):
        test_field = [[1,0,1,1],
                      [0,1,0,0],
                      [0,0,1,1],
                      [1,1,1,1]]
        sim = LifeSimulation(test_field)

        self.assertEqual(sim._get_alive_cells_around(1,1), 3)
        self.assertEqual(sim._get_alive_cells_around(1,2), 5)
        self.assertEqual(sim._get_alive_cells_around(2,1), 5)
        self.assertEqual(sim._get_alive_cells_around(2,2), 5)

    def test_counting_alive_cells_on_edges(self):
        test_field = [[1,0,1,1],
                      [0,1,0,0],
                      [0,0,1,1],
                      [1,1,1,1]]
        sim = LifeSimulation(test_field)

        self.assertEqual(sim._get_alive_cells_around(0,0), 1)
        self.assertEqual(sim._get_alive_cells_around(0,1), 3)
        self.assertEqual(sim._get_alive_cells_around(0,1), 3)
        self.assertEqual(sim._get_alive_cells_around(0,3), 1)
        self.assertEqual(sim._get_alive_cells_around(2,0), 3)
        self.assertEqual(sim._get_alive_cells_around(3,3), 3)

    def test_counting_alive_cells_in_default_field(self):
        alive_cells_around_center_cell = 4

        self.assertEqual(self.default_sim._get_alive_cells_around(1, 1), alive_cells_around_center_cell)

    def test_that_single_cell_always_dies(self):
        single_cell = [[1]]
        sim = LifeSimulation(single_cell)
        any_generations = 3
        sim.simulate_life(any_generations)

        self.assertEqual(sim.get_population_num(), 0)

    # https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns
    def test_oscillator_field(self):
        blinker_field = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        blinked_field = np.array([
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
        ])
        sim = LifeSimulation(blinker_field)

        sim.simulate_life(1)
        np.testing.assert_array_equal(sim.get_field(), blinked_field)

    def test_printint_field(self):
        self.default_sim.print_field()

    def test_default_field_after_first_generation(self):
        field_after_one_gen = np.array([
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,1,0,0,0],
            [0,1,1,0,0],
            [0,0,0,0,0],
        ])
        self.default_sim.simulate_life(1)
        np.testing.assert_array_equal(self.default_sim.get_field(), field_after_one_gen)

        field_after_two_gens = np.array([
            [0,0,1,0,0],
            [0,1,1,0,0],
            [1,0,0,1,0],
            [0,1,1,0,0],
            [0,0,0,0,0],
        ])
        self.default_sim.simulate_life(1)
        np.testing.assert_array_equal(self.default_sim.get_field(), field_after_two_gens)


    def test_solution(self):
        # generations = 10*10**9
        generations = 100
        self.default_sim.simulate_life(generations)
        print(f'Population after {generations} generations: {self.default_sim.get_population_num()}')


# check field shrinking

if __name__ == '__main__':
    unittest.main()
