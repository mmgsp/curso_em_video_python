import urllib.error, urllib.request

def verificaSite(link):
    req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        urllib.request.urlopen(req, timeout=10)
    except urllib.error.HTTPError as e:
        print(f"O site respondeu, mas rejeitou o Python. Código do erro: {e.code}")
    except urllib.error.URLError:
        print("Erro de conexão (Sem internet ou DNS inválido)")
    else:
        print("Conectado")
