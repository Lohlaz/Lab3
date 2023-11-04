import price_info

def test_cost_of_fruit():
    test_fruit = 'apple'
    test_quantity = 10
    results = price_info.cost_of_fruits(test_fruit, test_quantity)
    assert (results == 12)

def test_total_cost_shopping():
    test_fruit2 = 'apple'
    results = price_info.total_cost_shopping(test_fruit2)
    assert (results == 6)
