import pytest
import unittest
from http import HTTPStatus
from app.Products.forms.Product_form import MyForm

def test_form(app, test_client):    
    resp=test_client.post('/products/add-product',data=dict(name="test", price=0, color="white", description="Desc", category_id=0), 
    follow_redirects=True)
    
    assert resp.status_code == HTTPStatus.OK