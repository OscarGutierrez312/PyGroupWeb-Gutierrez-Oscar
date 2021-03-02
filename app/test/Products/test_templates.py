import pytest

def test_products_route_status_code_number1(test_client, captured_templates):
    route = "products/add-product"
    rv = test_client.get(route)

    assert rv.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "product_ex.html"

def test_category_route_status_code_number2(test_client, captured_templates):
    route = "products/add-category"
    rv = test_client.get(route)

    assert rv.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "category.html"

def test_catalogue_route_status_code_number3(test_client, captured_templates):
    route = "products/list/1"
    rv = test_client.get(route)

    assert rv.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "catalogue.html"