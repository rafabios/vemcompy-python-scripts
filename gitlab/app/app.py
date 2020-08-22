#!/usr/bin/python
# -*- coding: utf-8 -*-
######################################################################
# Simples Web Server em python!
# Criado em 31/03/2019
# Criado por: Rafael Souza
#
# Passar os seguintes dados como variavel de ambiente:
#
# WEBSERVICE_PORT     (INFORMAR PORTA TCP)
# WEBSERVICE_NAME     (INFORMAR NOME DO WEB SERVER)
# WEBSERVICE_VERSION  (INFORMAR A VERSAO)
#
######################################################################

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import socket
import time


# Checa se porta esta vazia, se, sim, sobe na porta 3000
try:
    int(os.getenv('WEBSERVICE_PORT'))
    PORT_NUMBER = int(os.getenv('WEBSERVICE_PORT'))
except:
    PORT_NUMBER = 3000


# Checa se cor de fundo esta vazia, se sim, sobe com cor branca
if str(os.getenv('WEBSERVICE_BGCOLOR')) == "None":
    WEBSERVICE_BGCOLOR = "white"  
else:
    WEBSERVICE_BGCOLOR = str(os.getenv('WEBSERVICE_BGCOLOR'))
     


#HOSTNAME = str(socket.gethostname())
#DATE = str(time.ctime())

MESSAGE = \
    '''
<html>
<head><title>PYTHON WEB SERVER</title></head>
<body bgcolor="{0}">
<center>
<h1> LUDONEWS - NOTICIAS</H1>
<br><br><br><br><br>






<br><br>
</center>
<br><br><br><br><br><br><br><br><br><br><br>

</body>
</html>
'''.format(WEBSERVICE_BGCOLOR)


# This class will handles any incoming request from
# the browser

class myHandler(BaseHTTPRequestHandler):

        # Handler for the GET requests

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

                # Send the html message

        self.wfile.write(MESSAGE)
        return


try:

        # Create a web server and define the handler to manage the
        # incoming request

    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Iniciando o webserver na porta: ', str(PORT_NUMBER))

        # Wait forever for incoming htto requests

    server.serve_forever()
except KeyboardInterrupt:

    print('^C received, shutting down the web server')
    server.socket.close()
