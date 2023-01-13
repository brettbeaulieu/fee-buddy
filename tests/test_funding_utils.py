import unittest

from . import (
    first_funding_period,
    most_recent_funding,
    funding_times,
    get_funding_periods,
    get_period_distance,
    get_funding_page,
)


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
