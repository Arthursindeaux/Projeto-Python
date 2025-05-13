# get-pip.py
import os
import sys
import urllib.request

def download_pip():
    url = "https://bootstrap.pypa.io/get-pip.py"
    print("Baixando o instalador do pip...")
    urllib.request.urlretrieve(url, "get-pip-downloaded.py")
    print("Arquivo salvo como get-pip-downloaded.py")
    print("Executando o instalador do pip...")
    os.system(f'"{sys.executable}" get-pip-downloaded.py')

if __name__ == "__main__":
    download_pip()
