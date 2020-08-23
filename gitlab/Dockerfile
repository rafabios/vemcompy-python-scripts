# Informar imagem
FROM python:2.7-alpine

# Copia o arquivo de webserver para a imagem a ser gerada
COPY app/*.py /opt/app/
COPY requirements.txt /opt/app/

# Informa o diretorio raiz da imagem -
WORKDIR /opt/app

# Instala requirements
RUN pip install -r requirements.txt

# Roda o webserver
CMD  python app.py
