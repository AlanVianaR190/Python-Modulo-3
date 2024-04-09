from urllib import request
import urllib
try:
    site=request.urlopen("http://www.pudim.com.br/")
except urllib.error.URLError:
    print("O site pudim não esta acessivel no momento!")
else:
    print("O site pudim esta Acessivel")

