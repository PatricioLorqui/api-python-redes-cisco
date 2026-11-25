# Entorno de virtualización Python

# Pasos de instalación en Linux:

## 1. Clonación del proyecto

Desde la terminal ejecutar:

**git clone** <URL_del_repositorio> <nombre_de_la_carpeta_de_destino>

Luego ejecutar **cd** <nombre_de_la_carpeta_de_destino>. Esta carpeta será la raíz de nuestro proyecto en Python.

## 2. Creación del entorno virtual

Supongamos que el nombre que le damos al entorno virtual es **cisco**, entonces se creará una carpeta **cisco** con todas las librerías y dependencias necesarias paea nuestro proyecto. 

La manera de realizarlo es la siguiente:

# python3 -m venv <nombre_del_entorno>
Ejemplo: python3 -m venv cisco

Para activar el entorno escribimos **source cisco/bin/activate**, en la carpeta raíz del proyecto. El nombre del entorno virtual aparecerá entre paréntesis ().

## 3. Instalación de las dependencias, en este caso las librerías requests y tabulate

En la carpeta raíz de nuestro proyecto y dentro del entorno virtual escribimos: **pip install -r requirements.txt**

## 4. Selección del intérprete Python para nuestro entorno virtual

<img width="881" height="118" alt="image" src="https://github.com/user-attachments/assets/18c41d8e-d338-48b6-953c-b2499c57319f" />

<img width="736" height="412" alt="image" src="https://github.com/user-attachments/assets/2a795fcd-2cf8-47ef-a5a6-d21e09ce967f" />

Tal como se ve en la figura seleccionamos Python 3.10.12 (cisco) que se mostrará como entorno recomendado.

## 5. Desactivación del entorno virtual

Simplemente escribimos en la línea de comandos: **deactivate**

## 6. Qué hacen los scripts?

Script 1: 01_get-ticket.py.
Método: POST.
Endpoint: /ticket
Descripción: Identifica con el controlador y devuelve el Token que usan las demás peticiones.


Script 2: 02_get-network-device.py.
Método: GET.
Endpoint: /network-device.
Descripción: Utiliza el token como header, el network controller responde con los dispositivos descubiertos en la red y son impresos en pantalla tal que, NOMBRE_DISPOSITIVO PLATAFORMA DIRECCION_IP.


Script 3: 03_get-host.py.
Método: GET.
Endpoint: /host
Descripción: Imprime por pantalla todos los hosts de la red con el siguiente formato: NOMBRE_HOST IP_HOST MAC_HOST PUERTO/INTERFAZ.


Script 4: 04_tabulate.py.
Método: GET/POST.
Endpoints: /ticket - /host - /network-device.
Descripción: Imprime en forma de tabla los Hosts con el siguiente formato: NOMBRE_HOST TIPO IP.


Script 5: inventory_csv.py.
Método: GET.
Endpoints: /host - /network-device.
Descripción: Lista hosts en red en un archivo CSV con el siguiente formato: TIPO IP_HOST MAC_HOST PLATAFORMA.
Este archivo está codificado en utf-8-sig.


## Antes de ejecutar los scripts

- **Credenciales del controlador:** Las credenciales fueron cambiadas a `cisco` y la clave `cisco123`. Esto es necesario para los scripts `01_get-ticket.py` y `04_tabulate.py`.
- **Ticket (X-Auth-Token):** Para todos los scripts es necesario generar un token nuevo ya que este es específico de cada sesión.
