import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'app-name':'AQUI_NOMBRE_APP',
     'voice':'AQUI_TIPO_DE_VOZ',
     'retries':'AQUI_NUMERO_DE_INTENTOS',
     'country-code':'CO',
     'phone':'AQUI_EL_NUMERO_DE_CELULAR'
}

r = requests.post('https://www.onurix.com/api/v1/call/2fa/send-call', headers = headers, data = data)

print(r.json())