from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_x_is_positive(self):
        assert sum_solution(-1, 2) == 

