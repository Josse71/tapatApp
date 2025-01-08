[INICIO](README.md)

# Requeriments tècnics

## 1. Backend (Servidor i Gestió de Dades)
El backend serà el cor del sistema, encarregat de gestionar dades, usuaris, i la lògica del sistema.

### a. Requisits del servidor
- Allotjament: Hosting Compartido.
- Base de dades: MYSQL.
- Sistema operatiu del servidor: Linux.
- APIs i serveis web: RESTFul Flask.

### b. Llenguatges de programació
- Flutter.

### c. Seguretat
- Autenticació i autorització: Mediante login y doble verificación con el móvil/email.
- Xifratge de dades: HASH.
- Còpies de seguretat automàtiques: Sí, cada X horas o días a elección del usuario.

## 2. Frontend
### a. Tipus de Clients
- Web, móviles y escritorio.
- Llenguatge de programació: HTML5, CSS y JS.
- Compatibilitat dispositius: Ha de ser compartido entre móviles y escritorio.

## 3. Requisits Generals
### a. Gestió d'usuari i autenticació
- Rols d’usuari: Administrador - Cuidador - Padre/Madre.
- Base de dades: MYSQL
- Seguretat: Login con función de doble verificación.

### b. Emmagatzematge local i sincronització
- Dades que es guarden en local, són sensibles? Sí, la información proporcionada por los tutores de guardan localmente.
- Seguretat: Mediante cifrado, FACE ID y/o huella dactilar.

### c. Gestió d’accessibilitat
- Nivells A, AA y AAA d’accessibilitat: AA.

## 4. Requisits d'Infraestructura
- Xarxa: HTTP.
- Espai d’emmagatzematge al núvol: Google Drive.
- APIs de tercers: Google Dirve.

## 5. Requisits del Procés de Desenvolupament
- IDE’s: Visual Studio Code, 
- Control de Versions: Git y GitHub.
- Mètode de desenvolupament: Seguir una metodologia àgil com Scrum per iterar i validar funcionalitats amb usuaris reals.
- Proves de qualitat (QA): Tests
