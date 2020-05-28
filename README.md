# Crawler en Python con las Fases de la desescalada en España

La aplicación usa [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) para leer la web oficial de las fases de desescalada [Link](https://www.lamoncloa.gob.es/covid-19/Paginas/mapa-fases-desescalada.aspx) y disponibiliza los datos en una API Rest

Los siguientes pasos despliegan la aplicación en [IBM Cloud](cloud.ibm.com)

## Prerequisitos

Necesitarás lo siguiente:
* [Cuenta IBM Cloud](https://console.ng.bluemix.net/registration/)
* [Cloud Foundry CLI](https://github.com/cloudfoundry/cli#downloads)
* [Git](https://git-scm.com/downloads)
* [Python](https://www.python.org/downloads/)

## 1. Clona la aplicación

Clona el repositorio y cambia al directorio donde se localiza la aplicación de ejemplo.

  ```
git clone https://github.com/mariaborbones/crawler_territorios_fases
cd fases-desescalada
  ```

## 2. Ejecuta la aplicación localmente

Instala las dependencias que se detallan en [requirements.txt](https://pip.readthedocs.io/en/stable/user_guide/#requirements-files) para ser capaz de ejecutar la aplicación


  ```
pip install -r requirements.txt
  ```

Ejecutar la aplicación
  ```
python hello.py
  ```

 Puedes ver la aplicación en: http://localhost:8000


## 3. Prepara la aplicación para desplegarla

Para desplegarla en IBM Cloud, es útil añadir un fichero manifest.yml. Ya se incluye uno en este repositorio como ejemplo.

El manifest.yml incluye información básica de tu aplicación, como el nombre, cuanta memoria alojar para cada instancia y la ruta. En el manifest.yml **random-route: true** genera una ruta aleatoria para asegurarnos que no colisiona con otras aplicaciones existentes en IBM Cloud.  Puedes reemplazar **random-route: true** con **host: miNombreDeHost**, sustituyendo el nombre del Host por el que tu quieras. [Más info en...](https://console.bluemix.net/docs/manageapps/depapps.html#appmanifest)
 ```
 applications:
 - name: APIFases
   random-route: true
   memory: 128M
 ```

## 4. Despliegue de la aplicación

Puedes usar Cloud Foundry para desplegar la aplicación

Elige tu endpoint
   ```
bx api <API-endpoint>
   ```

Reemplaza *API-endpoint* en el comando con el endpoint elegido de la siguiente lista .

|URL                             |Region          |
|:-------------------------------|:---------------|
| https://api.ng.bluemix.net     | US South       |
| https://api.eu-de.bluemix.net  | Germany        |
| https://api.eu-gb.bluemix.net  | United Kingdom |
| https://api.au-syd.bluemix.net | Sydney         |

Haz login en tu cuenta de IBM Cloud

  ```
bx login
  ```

Desde tu repositorio de  *fases-desescalada* haz push de la aplicación a IBM Cloud
  ```
bx app push
  ```

Puede tardar unos minutos. Si quieres ver los logs puedes ejecutar `bx logs <Your-App-Name> --recent`
