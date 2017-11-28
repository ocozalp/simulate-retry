from unittest.case import TestCase

from impl.simple_timeline import SimpleTimeline


class TestSimpleTimeline(TestCase):

    def test_non_overlapping_events(self):
        under_test = SimpleTimeline(1000)
        under_test.inc(1, 100, 1)
        under_test.inc(101, 200, 1)

        self.verify_interval(under_test, 1, 200, 1)

    def test_overlapping_events(self):
        under_test = SimpleTimeline(1000)

        under_test.inc(1, 100, 1)
        under_test.inc(50, 200, 1)

        self.verify_interval(under_test, 1, 49, 1)
        self.verify_interval(under_test, 50, 100, 2)
        self.verify_interval(under_test, 101, 200, 1)

    def verify_interval(self, under_test, start, end, target_val):
        for i in xrange(start, end + 1):
            self.assertEqual(target_val, under_test.get(i))
