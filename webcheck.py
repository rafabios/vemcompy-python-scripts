
import requests
import sites

urls = sites.urls

def webcheck(urls):
    lista = []
    for url in urls:
        try:
            web = requests.get(url)
            status_code = str(web.status_code)[0]
            print_code = str(web.status_code)
        except:
            status_code = '900'
            print_code  = '900'

        if status_code == '2' or status_code == '3':
            status = print_code + ':Site ok: '
            lista.append(status + url)
        else:
            status = print_code + ':Site com problemas: '
            lista.append(status + url)
    return lista

webprint = webcheck(urls)

print(*webprint, sep='\n')
