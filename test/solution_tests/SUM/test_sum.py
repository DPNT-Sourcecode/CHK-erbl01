import pytest
from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_x_cant_be_negative(self):
        with pytest.raises(ValueError):
            sum_solution.compute(-1, 2)

    def test_x_cant_be_more_than_100(self):
        with pytest.raises(ValueError):
            sum_solution.compute(101, 2)
            

