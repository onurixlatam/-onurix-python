import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'template':'AQUI_EL_NOMBRE_DE_LA_PLANTILLA',
     'content':'AQUI_EL_JSON_CON_LOS_VALORES_PARA_LA_PLANTILLA'
}

r = requests.post('https://www.onurix.com/api/v1/whatsapp/shopify/order', headers = headers, data = data)

print(r.json())