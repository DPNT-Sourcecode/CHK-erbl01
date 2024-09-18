from solutions.HLO import hello_solution


class TestHello():
  def test_hello(self):
    name = "Craftsman"
    assert hello_solution.hello(name) == f"Hello, {name}!"