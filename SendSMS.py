import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'phone':'AQUI_EL_NUMERO_DE_CELULAR',#PARA ENVIAR MULTIPLES TELEFONOS TENDRAN QUE SER SEPARADOS POOR COMAS ","
     'sms':'AQUI_EL_SMS_A_ENVIAR',
     'groups':"AQUI_ID_GRUPOS",#PARA ENVIAR MULTIPLES GRUPOS TENDRAN QUE SER SEPARADOS POOR COMAS ","
     }
r = requests.post('https://www.onurix.com/api/v1/send-sms', headers = headers, data = data)

print(r.json())