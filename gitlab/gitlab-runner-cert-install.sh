#!/bin/bash

# Instala o runner em distribuicoes baseadas em debian
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash || true

# Instala o runner em distribuicoes baseadas em centos
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh | sudo bash || true

# Alterar esse valor para seu endereco
SERVER=gitlab.vemcompy.net
PORT=443
CERTIFICATE=/etc/gitlab-runner/certs/${SERVER}.crt

# Create the certificates hierarchy expected by gitlab
sudo mkdir -p $(dirname "$CERTIFICATE")

# Get the certificate in PEM format and store it
openssl s_client -connect ${SERVER}:${PORT} -showcerts </dev/null 2>/dev/null | sed -e '/-----BEGIN/,/-----END/!d' | sudo tee "$CERTIFICATE" >/dev/null

# Register your runner
gitlab-runner register --tls-ca-file="$CERTIFICATE"
