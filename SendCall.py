import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'phone':'AQUI_EL_NUMERO_DE_CELULAR',
     'message':'AQUI_EL_MENSAJE_A_ENVIAR',
     'voice':'AQUI_TIPO_DE_VOZ',
     'retries':'AQUI_NUMERO_DE_INTENTOS',
     'leave-voicemail':'false',
     #'audio-code':'AQUI_ID_AUDIO',
     'country-code':'CO'
}

r = requests.post('https://www.onurix.com/api/v1/call/send', headers = headers, data = data)

print(r.json())