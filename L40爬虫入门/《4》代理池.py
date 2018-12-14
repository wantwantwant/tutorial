



import urllib.request

def get_proxy():
    resp =urllib.request.urlopen('http://192.168.221.221:5010/get')
    proxy =resp.read().decode()
    return proxy
