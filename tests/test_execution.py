from unittest import TestCase

import progress_printer as pp
import datetime

class TestProgressPrinter(TestCase):
    def test_errorless_execution(self):
        return_value = 1
        a=range(1000)
        t0 = datetime.datetime.now()
        for i in a:
            pp.ProgressStatus(i, 1000, t0)
        return_value = 0
        self.assertTrue(return_value == 0.0)
