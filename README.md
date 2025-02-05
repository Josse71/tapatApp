# TAPATAPP 24-25 PÚBLICO

[DESCRIPCIÓN TAPATAPP](descTapatapp.md)

[REQUERIMIENTOS TÉCNICOS](requerimientosTecnicos.md)

[HTTP REQUEST](httpRequest.md)

[HTTP RESPONSE](httpResponse.md)

## Definició dels EndPoints del Servei Web:

- Descripció: Servicio que consulta un Usuario por username.
- HOST: 192.168.144.132:10050
- End-Point: http://192.168.144.132:10050/tapatapp/getUser
- Method: GET
- Parameters: username
- Resposta: 

- Còdigos de Resposta HTTP:

### 1. Code 200 Ok:
{
"status": "success",
"data": {
"username": "usuari1",
"firstName": "Nom",
"lastName": "Cognom",
"email": "usuari1@example.com",
"phone": "123456789",
"address": "Carrer Mor, 123"
}
}

### 2. 400 Bad Request - La sol·licitud està mal formada o li falten paràmetres:
{
"status": "error",
"message": "Paràmetre 'username' no proporcionat o incorrecte"
}
### 3. 401 Unauthorized - No s'ha autenticat correctament:
{
"status": "error",
"message": "No autoritzat. Necessites autenticar-te per accedir a aquesta informació."
}
### 4. 403 Forbidden - L'usuari no té permís per consultar la informació:
{
"status": "error",
"message": "Accés prohibit. No tens permís per veure aquesta informació."
}

### 5. 404 Not Found - L'usuari no es troba a la base de dades:
{
"status": "error",
"message": "Usuari no trobat"
}
### 6. 422 Unprocessable Entity - La sol·licitud està ben formada, però el servidor no pot processar la informació proporcionada (per exemple, si el nom d'usuari té un format invàlid):
{
"status": "error",
"message": "Format de 'username' invàlid.
Si us plau, revisa el teu input."
}

### 7. 500 Internal Server Error - S'ha produït un error intern al servidor:
{
"status": "error",
"message": "Error intern al servidor. Si us plau, torni-ho a provar més tard."
}
# URL per provar totes les possibles sortides:
http://192.168.144.132:10050//tapatapp/getUser?name=usuari1