
from fastapi.testclient import TestClient
from main_auth import app

#usuarios registrados en el sistema con nombre y contraseña.
usuario_ok = {"nombre":"pepeLuis", "contraseña":"12345"}
usuario_credencial_invalida = {"nombre":"pepeLuis", "contraseña":"12"}
usuario_invalido = {"nombre":"marcoaurelio", "contraseña":"dd12345"}
    
client=TestClient(app)

def test_get_raiz():
    response=client.get("/")
    assert response.status_code==200

def test_login_usuario_registrado():
    response=client.post("/login", json=usuario_ok)
    assert response.status_code==200

def test_login_usuario_no_registrado():
    response=client.post("/login", json=usuario_invalido)
    assert response.status_code==401

def test_login_usuario_registrado_credenciales_invalidas():
    response=client.post("/login", json=usuario_credencial_invalida)
    assert response.status_code==401

def test_verificar_token_ok():
    response=client.post("/login", json=usuario_ok)
    assert response.status_code==200
    response_data=response.json()
    access_token=response_data["access_token"]
    response=client.get(f"/verificar_token?token={access_token}")
    assert response.status_code==200

def test_verificar_token_invalido():
    response=client.post("/login", json=usuario_ok)
    assert response.status_code==200
    response_data=response.json()
    access_token=response_data["access_token"]
    #MOdifico el token valido aproposito
    response=client.get(f"/verificar_token?token=modified{access_token}")
    assert response.status_code==401
