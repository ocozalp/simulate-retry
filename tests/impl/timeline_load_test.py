from unittest.case import TestCase
from impl.fenwick_tree import FenwickTree
from impl.timeline import Timeline, SimpleTimeline
import random
import time

class TimelineLoadTest:
    type = Timeline

    def test_big_interval_1000_short_events(self):
        now = time.time()
        self.__load_test(10000000, 100, 200, 1000)
        print time.time() - now

    def test_medium_interval_long_duration_20000_events(self):
        now = time.time()
        self.__load_test(100000, 900, 1000, 20000)
        print time.time() - now

    def test_big_interval_long_duration_100000_events(self):
        now = time.time()
        self.__load_test(1000000, 100, 10000, 100000)
        print time.time() - now

    def __load_test(self, max_val, min_duration, max_duration, event_count):
        random.seed(1000000007)
        under_test = self.type(max_val)
        for i in xrange(event_count):
            duration = random.randrange(min_duration, max_duration)
            start = random.randrange(1, max_val - max_duration)
            under_test.inc(start, start + duration, 1)

class SimpleTimelineLoadTests(TimelineLoadTest, TestCase):
    type = SimpleTimeline

class FenwickTreeLoadTests(TimelineLoadTest, TestCase):
    type = FenwickTree