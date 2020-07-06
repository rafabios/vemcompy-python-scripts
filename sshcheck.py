
from SSHLibrary import SSHLibrary

import sshlista

lista = sshlista.ssh

def service_check(hostname,login,password):

    ssh = SSHLibrary()

    try:
        ssh.open_connection(hostname)
        ssh.login(login, password)
    except:
        print('Erro ao conectar no host!')

    ssh_command = ssh.execute_command('systemctl status nginx')

    if str(ssh_command).find('(running)') != -1 :
        status = 'Servico ok!'
    else:
        status = 'Servico com problemas!'

    return status


for l in lista.items():
    alias = l[0]
    hostname = l[1][0]
    login    = l[1][1]
    password = l[1][2]
    print(alias)
    print(service_check(hostname,login,password))


    
