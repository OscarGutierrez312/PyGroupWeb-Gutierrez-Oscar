import pytest
import unittest
from http import HTTPStatus


def test_auth_route_status_code_(test_client, captured_templates):
    route = "auth/login"
    rv = test_client.get(route)

    assert rv.status_code == HTTPStatus.OK
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "login.html"

def test_authentication(app, test_client):    
    dat={
        'email':'testemail@mail.com',
        'password':123456789
    }

    rv=test_client.post('/auth/login', data=dict(
        email=dat['email'],
        password=dat['password']
    ), follow_redirects=True)
  
    assert rv.status_code == HTTPStatus.OK

    rv=test_client.get('/auth/logout', follow_redirects=True)
    assert rv.status_code == HTTPStatus.OK

    rv=test_client.post('/auth/login', data=dict(
        email=dat['email'],
        password=dat['password']
    ), follow_redirects=True)

    assert b'Please check your login details and try again.' in rv.data

    rv=test_client.post('/auth/login', data=dict(
        email=dat['email'],
        password=dat['password']
    ), follow_redirects=True)

    assert b'Please check your login details and try again.' in rv.data




