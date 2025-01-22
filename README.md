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

Code 200 Ok: {id=1,"username":"josse", "password":"gomez", "email":"josegomez99@gmail.com"}

Code 400 No trobat: {"error": "No trobat"}