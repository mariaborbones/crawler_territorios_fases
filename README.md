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

To deploy to IBM Cloud, it can be helpful to set up a manifest.yml file. One is provided for you with the sample. Take a moment to look at it.

The manifest.yml includes basic information about your app, such as the name, how much memory to allocate for each instance and the route. In this manifest.yml **random-route: true** generates a random route for your app to prevent your route from colliding with others.  You can replace **random-route: true** with **host: myChosenHostName**, supplying a host name of your choice. [Learn more...](https://console.bluemix.net/docs/manageapps/depapps.html#appmanifest)
 ```
 applications:
 - name: GetStartedPython
   random-route: true
   memory: 128M
 ```

## 4. Deploy the app

You can use the Cloud Foundry CLI to deploy apps.

Choose your API endpoint
   ```
cf api <API-endpoint>
   ```

Replace the *API-endpoint* in the command with an API endpoint from the following list.

|URL                             |Region          |
|:-------------------------------|:---------------|
| https://api.ng.bluemix.net     | US South       |
| https://api.eu-de.bluemix.net  | Germany        |
| https://api.eu-gb.bluemix.net  | United Kingdom |
| https://api.au-syd.bluemix.net | Sydney         |

Login to your IBM Cloud account

  ```
cf login
  ```

From within the *get-started-python* directory push your app to IBM Cloud
  ```
cf push
  ```

This can take a minute. If there is an error in the deployment process you can use the command `cf logs <Your-App-Name> --recent` to troubleshoot.

When deployment completes you should see a message indicating that your app is running.  View your app at the URL listed in the output of the push command.  You can also issue the
  ```
cf apps
  ```
  command to view your apps status and see the URL.
