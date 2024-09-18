from solutions.CHK import checkout_solution


class TestCHK():
  def test_price_of_one_item(self):
    assert checkout_solution.checkout("A") == 50

  def test_invalid_item(self):
    assert checkout_solution.checkout("ZDDDD") == -1