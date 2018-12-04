import unittest
import drone_flight_planner_review as d


class TestDroneFlightPlanner(unittest.TestCase):

    def setUp(self):
        self.example1 = [[1,2,3],[4,5,6],[7,8,9]]
        self.example2 = [[4,5,6],[3,4,2],[3,2,1]]

    def test_return_zero_if_maximum_is_initial(self):
        # setup
        expected = 0

        # execute
        result = d.calc_drone_min_energy(self.example2)

        # verify
        self.assertEqual(result, expected)

    def test_return_non_zero_value_if_maximum_is_greater_than_initial(self):
        # setup
        expected = 6

        # execute
        result = d.calc_drone_min_energy(self.example1)

        # verify
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
