from solutions.CHK import checkout_solution


class TestCHK():
  def test_invalid_item(self):
    assert checkout_solution.checkout("1") == -1

  def test_all_normal_and_offers(self):
    for sku, offers in checkout_solution.PRICES.items():
      for offer in offers:
        assert checkout_solution.checkout(sku*offer["units_required"]) == offer["price"]

  def test_buy_x_get_y_free(self):
    for sku, offer in checkout_solution.BUY_X_GET_Y_FREE.items():
      items = offer["item_required"]*offer["units_required"]+sku
      required_item_price = checkout_solution.PRICES[offer["item_required"]][-1]["price"]
      expected_price = required_item_price*offer["units_required"]
      assert checkout_solution.checkout(items) == expected_price

  






