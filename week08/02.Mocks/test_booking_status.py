import unittest
from unittest.mock import Mock, patch
from booking_status import get_booking_status
from datetime import datetime


class TestGetBookingStatus(unittest.TestCase):
    def test_if_it_booking_is_cancelled(self):
        booking = Mock(cancelled=True)
        result = get_booking_status(booking)
        self.assertEqual(result, 'Cancelled')

    @patch('booking_status.datetime')
    def test_if_all_conditions_are_false(self, datetime_mock):
        booking = Mock(cancelled=False, start=datetime(year=2020, month=4, day=16))
        booking.is_fully_paid.return_value = False
        datetime_mock.now.return_value = datetime(year=2020, month=4, day=17)
        result = get_booking_status(booking)
        self.assertEqual(result, 'Waiting taxes')

    def test_if_booking_is_paid(self):
        booking = Mock(cancelled=False)
        result = get_booking_status(booking)
        self.assertEqual(result, 'Paid')


if __name__ == '__main__':
    unittest.main()
