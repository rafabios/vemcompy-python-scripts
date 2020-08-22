#!/bin/bash

# Criar pasta e dar permissoes para a mesma
mkdir ssl
chmod -R 777 ssl
cd ssl/


# Gerar certicado

openssl genrsa -out server.key 2048
openssl rsa -in server.key -out server.key
# Modificar linha abaixo!
openssl req -sha256 -new -key server.key -out server.csr -subj '/CN=gitlab.vemcompy.net'
openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt
