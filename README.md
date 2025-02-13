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
### URL per provar totes les possibles sortides:
http://192.168.144.132:10050//tapatapp/getUser?name=usuari1

## Diagrama de Flujo - Pantallas tapatApp

[Diagrama de flujo](pantallasTapatApp.mermaid)

## Datos de entrada del usuario

### Inicio

- Contacta con nosotros: Esta pantalla le permite al usuario mandar un mensaje al equipo de soporte ténico especificando su duda/problema. La pantalla tiene un formulario en el que debe poner su correo y un mensaje.
- Registro: El usuario debe registrarse únicamente con un correo electrónico válido y una contraseña que incluya letras y números.
- Login: El login se hará mediante un email y una contraseña.
- - He olvidado mi contraseña: En caso de que el usuario no se acuerde de su clave, en esta pantalla puede recuperarla poniendo el correo con el que se registró. Se le enviará un enlace en el que puede cambiar la contraseña.

### Pantalla principal

- Niños a cargo: Aquí se muestra el listado de infantes bajo el cuidado del usuario.
- - Horas activas del pegat: Se le muestra al usuario la información con respecto al pegat sobre el niño/a a cargo (horas colocado, hora a retirar/colocar).
- Configuración: El usuario puede realizar ciertas configuraciones.
- - Editar perfil: Aquí el usuario puede modificar sus datos personales, añadir nueva información o actualizar cuaqluier apartado personal que desee.
- - Configuraciones generales: Aquí se puede personalizar el aspecto de la aplicación (modo oscuro, tamaño de texto).
- Cerrar sesión: El usuario deberá confirmar que quiere cerrar sesión.