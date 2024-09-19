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
      print(offer["item_required"]*offer["units_required"]+sku)
      assert checkout_solution.checkout(offer["item_required"]*offer["units_required"]+sku) == checkout_solution.PRICES[offer["item_required"]][-1]["price"]*offer["units_required"]

  





