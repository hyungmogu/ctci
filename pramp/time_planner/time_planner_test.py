import unittest
import time_planner as t

class TestTimePlanner(unittest.TestCase):
    def setUp(self):
        self.example1_slotA = [[10,50],[60,120],[140,210]]
        self.example1_slotB = [[0,15],[60,70]]
        self.example1_dur = 24

        self.example2_slotA = [[10,50],[60,120]]
        self.example2_slotB = [[0,5],[55,60]]
        self.example2_dur = 12

        self.example3_slotA = [[10,50],[60,120],[140,210]]
        self.example3_slotB = [[0,15],[60,70]]
        self.example3_dur = 8

    def test_return_empty_list_when_duration_is_bigger_than_available_time(self):
        expected = []
        result = t.meeting_planner(self.example1_slotA, self.example1_slotB, self.example1_dur)
        self.assertEqual(expected, result)

    def test_return_empty_list_when_there_are_no_available_time(self):
        expected = []
        result = t.meeting_planner(self.example2_slotA, self.example2_slotB, self.example2_dur)
        self.assertEqual(expected, result)

    def test_return_time_slots_when_time_is_available(self):
        expected = [60, 68]
        result = t.meeting_planner(self.example3_slotA, self.example3_slotB, self.example3_dur)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()