from solutions.CHK import checkout_solution


class TestCHK():
  def test_invalid_item(self):
    assert checkout_solution.checkout("ZDDDD") == -1

  def test_price_of_one_item(self):
    assert checkout_solution.checkout("A") == 50

  def test_a_special_offer_price(self):
    assert checkout_solution.checkout("AAA") == 130

  def test_a_special_offer_price_and_normal_price(self):
    assert checkout_solution.checkout("A"*4) == 130 + 50

  def test_b_price(self):
    assert checkout_solution.checkout("B") == 30

  def test_b_special_offer_price(self):
    assert checkout_solution.checkout("BB") == 45

  def test_b_special_offer_price_and_normal_price(self):
    assert checkout_solution.checkout("B"*5) == 120
  
  def test_c_price(self):
    assert checkout_solution.checkout("CCC") == 60

  def test_d_price(self):
    assert checkout_solution.checkout("DDD") == 45

  def test_multi_items_price(self): 
    assert checkout_solution.checkout("AAABBABCD") == 290
  
  def test_e_price(self):
    assert checkout_solution.checkout("EE") == 80

  def test_e_offer(self):
    assert checkout_solution.checkout("EEB") == 80
  
  def test_e_offer_and_b_special_price(self):
    assert checkout_solution.checkout("EEBBB") == 125
  
  def test