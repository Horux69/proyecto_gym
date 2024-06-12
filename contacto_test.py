import pytest
from unittest.mock import patch
from flask import session
from conexion import *
from models.contactanos import Datoscontacto

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def login_as_admin(client):
    with client.session_transaction() as sess:
        sess['logueado'] = True
        sess['rol'] = 'administrador'

def login_as_super_admin(client):
    with client.session_transaction() as sess:
        sess['logueado'] = True
        sess['rol'] = 'super_admin'

@patch.object(Datoscontacto, 'consultaDatosgym')
def test_contacto_get(mock_consultaDatosgym, client):
    mock_consultaDatosgym.return_value = []
    response = client.get('/contacto')
    assert response.status_code == 200
    assert b'contacto.html' in response.data

@patch.object(Datoscontacto, 'agregarDatosgym')
def test_agregarDatosgym_post_as_admin(mock_agregarDatosgym, client):
    login_as_admin(client)
    response = client.post('/contacto/agregar', data={
        'nombre_gym': 'Gym A',
        'telefono_gym': '123456',
        'correo_gym': 'gym@example.com',
        'ubicacion_gym': 'Ubicación A',
        'barrio_gym': 'Barrio A',
        'direccion_gym': 'Dirección A'
    })
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/contacto'
    mock_agregarDatosgym.assert_called_once()

@patch.object(Datoscontacto, 'agregarDatosgym')
def test_agregarDatosgym_post_as_super_admin(mock_agregarDatosgym, client):
    login_as_super_admin(client)
    response = client.post('/contacto/agregar', data={
        'nombre_gym': 'Gym A',
        'telefono_gym': '123456',
        'correo_gym': 'gym@example.com',
        'ubicacion_gym': 'Ubicación A',
        'barrio_gym': 'Barrio A',
        'direccion_gym': 'Dirección A'
    })
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/contacto'
    mock_agregarDatosgym.assert_called_once()

@patch.object(Datoscontacto, 'actualizarDatosgym')
def test_actualizarDatosgym_post_as_admin(mock_actualizarDatosgym, client):
    login_as_admin(client)
    response = client.post('/contacto/actualizar', data={
        'id_contacto': '1',
        'nombre_gym': 'Gym B',
        'telefono_gym': '654321',
        'correo_gym': 'gymb@example.com',
        'ubicacion_gym': 'Ubicación B',
        'barrio_gym': 'Barrio B',
        'direccion_gym': 'Dirección B'
    })
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/contacto'
    mock_actualizarDatosgym.assert_called_once()

@patch.object(Datoscontacto, 'actualizarDatosgym')
def test_actualizarDatosgym_post_as_super_admin(mock_actualizarDatosgym, client):
    login_as_super_admin(client)
    response = client.post('/contacto/actualizar', data={
        'id_contacto': '1',
        'nombre_gym': 'Gym B',
        'telefono_gym': '654321',
        'correo_gym': 'gymb@example.com',
        'ubicacion_gym': 'Ubicación B',
        'barrio_gym': 'Barrio B',
        'direccion_gym': 'Dirección B'
    })
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/contacto'
    mock_actualizarDatosgym.assert_called_once()

def test_agregarDatosgym_redirect_not_logged_in(client):
    response = client.post('/contacto/agregar')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/'

def test_actualizarDatosgym_redirect_not_logged_in(client):
    response = client.post('/contacto/actualizar')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/'
