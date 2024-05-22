from datetime import datetime
from fastapi.testclient import TestClient
from main_user import app as app_user
from main_auth import app as app_auth

#usuarios registrados en el sistema con nombre y contraseña.
usuario_ok = {"nombre":"pepeLuis", "contraseña":"12345"}
usuario_invalido = {"nombre":"marcoaurelio", "contraseña":"dd12345"}
    
client_user=TestClient(app_user)
client_auth=TestClient(app_auth)

"""
def test_get_raiz_token_valido():
    response=client_auth.post("http://localhost:8000/login", json=usuario_ok)
    assert response.status_code==200
    response_data=response.json()
    access_token="Bearer " + response_data["access_token"]
    
    headers = {
        "Authorization": access_token
    }
    print("xxxxxxxxxxxxxxxxx")
    print(headers)
    response=client_user.get("http://localhost:8001/",headers=headers)
    assert response.status_code == 200


def test_obtener_todos_usuarios_iniciales_igual_3():
    response=client_auth.post("/login", json=usuario_ok)
    assert response.status_code==200
    response_data=response.json()
    access_token="Bearer " + response_data["access_token"]
    
    headers = {
        "Authorization": access_token
    }

    response=client_user.get("/usuarios", headers=headers)
    assert response.status_code==200
    response_data=response.json()
    assert 3==len(response_data)
"""
