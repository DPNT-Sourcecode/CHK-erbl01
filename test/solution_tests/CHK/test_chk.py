from solutions.CHK import checkout_solution


class TestCHK():
  def test_invalid_item(self):
    assert checkout_solution.checkout("1") == -1

  def test_price_of_one_item(self):
    assert checkout_solution.checkout("A") == 50

  def test_a_special_offer_price(self):
    assert checkout_solution.checkout("AAA") == 130

  def test_a_special_offer_price_and_normal_price(self):
    assert checkout_solution.checkout("A"*4) == 180

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
  
  def test_a_bulk_special_offer_price(self):
    assert checkout_solution.checkout("A"*5) == 200

  def test_a_bulk_special_offer_price_and_special_price(self):
    assert checkout_solution.checkout("A"*8) == 330

  def test_a_bulk_special_offer_price_and_special_price_normal_price(self):
    assert checkout_solution.checkout("A"*9) == 380
  
  def test_multi_items_price_with_bulk_price(self):
    assert checkout_solution.checkout("A"*9 + "EEBBBDC") == 540
  
  def test_f_price(self):
    assert checkout_solution.checkout("F") == 10

  def test_f_offer(self):
    assert checkout_solution.checkout("FFF") == 20
  
  def test_f_offer_and_special_price(self):
    assert checkout_solution.checkout("FFFF") == 30
  
  def test_multi_items_with_f(self):
    assert checkout_solution.checkout("A"*9 + "EEBBBDCFFFF") == 570
  
  def check_prices(self, sku, expected_price):
    assert checkout_solution.checkout(sku) == expected_price

  def test_all(self):
    for sku, offers in checkout_solution.PRICES.items():
      for offer in offers:
        check_prices(self, sku*offer["units_required"], offer["price"])

  


