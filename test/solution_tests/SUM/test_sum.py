import pytest
from solutions.SUM import sum_solution


class TestSum():
    def test_sum_positive_numbers(self):
        assert sum_solution.compute(1, 2) == 3

    def test_x_cant_be_negative(self):
        with pytest.raises(ValueError):
            sum_solution.compute(-1, 2)

    def test_x_cant_be_more_than_100(self):
        with pytest.raises(ValueError):
            sum_solution.compute(101, 2)

    def test_y_cant_be_negative(self):
        with pytest.raises(ValueError):
            sum_solution.compute(1, -1)

    def test_y_cant_be_more_than_100(self):
        with pytest.raises(ValueError):
            sum_solution.compute(1, 101)

    def test_sum_negative_numbers(self):
        with pytest.raises(ValueError):
            sum_solution.compute(-1, -1)




