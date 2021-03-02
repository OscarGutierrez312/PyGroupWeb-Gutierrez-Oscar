import pytest
import pytest
import unittest
from http import HTTPStatus
from app.Products.forms.Product_form import MyForm

def test_cart_route_status_code_302(test_client, captured_templates):
   
    route = "/cart/MyCart"
    rv = test_client.get(route)

    assert rv.status_code == 302
    assert len(captured_templates) == 0
    


def test_form(app, test_client):    
    resp=test_client.post('/cart/add-in-car', data=dict(id=1), follow_redirects=True)
    
    assert resp.status_code == HTTPStatus.OK

def test_add(app, test_client):    
    resp=test_client.get('/cart/add/2', follow_redirects=True)    
    assert resp.status_code == HTTPStatus.OK

