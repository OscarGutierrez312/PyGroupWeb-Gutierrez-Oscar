

def test_main_route_status_code_number3(test_client, captured_templates):
    route = "products/add-product"
    rv = test_client.get(route)

    # Sanity checks - it would be a total surprise if this would not hold true
    assert rv.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "product_ex.html"
