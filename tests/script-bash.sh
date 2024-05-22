#!/bin/bash

set -e

echo "Ejecucion de pruebas de autenticacion"
#cd /app/autenticacion
pytest test_autenticacion.py --disable-warnings

echo "Ejecucion de pruebas de USUARIOS"
#cd /app/usuarios
pytest test_usuarios.py --disable-warnings