# Informar imagem
FROM python:2.7-alpine
# Copia o arquivo de webserver para a imagem a ser gerada
COPY app/app.py /opt/app/app.py
# Informa o diretorio raiz da imagem -
WORKDIR /opt/app
# Roda o webserver
CMD  python app.py
