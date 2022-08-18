import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'name':'AQUI_NOMBRE_DE_URL',
     'url-long':'AQUI_URL_LARGA'
}

r = requests.post('https://www.onurix.com/api/v1/url/short', headers = headers, data = data)

print(r.json())