import requests
headers = {'Content-type': 'application/json'}
r = requests.post("http://fme.pbh/fmerest/v3/transformations/transact/testes/BUSCAR_ACERVO.fmw?fmetoken=fa88907df0f8c04a9d7d366ebdbdd235b5c8d4e4",  headers=headers)

print(r.status_code)
print(r.headers)
print(r.content)