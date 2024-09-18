from solutions.CHK import checkout_solution


class TestCHK():
  def test_invalid_item(self):
    assert checkout_solution.checkout("ZDDDD") == -1

  def test_price_of_one_item(self):
    assert checkout_solution.checkout("A") == 50

  def test_A_special_offer_price(self):
    assert checkout_solution.checkout("AAA") == 130

  def test_A_special_offer_price_and_normal_price(self):
    assert checkout_solution.checkout("A"*7) == 310

  def 