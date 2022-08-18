import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'phone':'AQUI_EL_NUMERO_DE_CELULAR',
     'sms':'AQUI_EL_SMS_A_ENVIAR',
     'country-code':'CO'}

r = requests.post('https://www.onurix.com/api/v1/send-sms', headers = headers, data = data)

print(r.json())