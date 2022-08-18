import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'2412',
     'key':'582876138efc20d00c3bd32c046edff0cdd3369061d4c5123747d',
     'phone':'573203711034',
     'code':'ZJAH',
     'app-name':'PruebaSMS',
     'country-code':'CO'
}

r = requests.post('https://www.onurix.com/api/v1/2fa/verification-code', headers = headers, data = data)

print(r.json())