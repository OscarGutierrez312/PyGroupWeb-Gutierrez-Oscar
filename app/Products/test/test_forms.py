from wtforms_test import FormTestCase
from app.Products.forms.Product_form import MyForm

def test_form(app, test_client):    
    
    
    assert assert_requires('name')