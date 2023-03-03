import requests
import logging
import json
class ManageGovernor():
    def __init__(self): pass

    def start(self, id_Device):

        logging.info(" INICIANDO: ( ManageGovernor )")
        try:
            #* GET TOKEN AUTHENTICATION
            getToken = requests.post(
                url  = f'http://127.0.0.1:8000/api-token-auth/',
                json = {'username': 'root', 'password': 'root'}
            )

            if not getToken.status_code == 200:
                logging.info("No se ha podido encontrar el token:")
                response = {"status": getToken.status_code, 'data': {}}
                return response

            getToken = getToken.json()
            token    = getToken.get('token')
            header   = {'Authorization': 'token {}'.format(token)}

            packageDevice  = self.getPackage(id_Device, header)
            settingsDevice = self.getSettings(id_Device, header)

            return packageDevice, settingsDevice

        except Exception as e:
            logging.info("Ha ocurrido un error al usar el manageGovernor", e)

    def getPackage(self, id_Device, headers):
        logging.info("-----| Consultando Paquetes |------")

        #* GET INFO DEVICE
        try:
            #API request
            dataDevice  = requests.get(
                url     = f'http://127.0.0.1:8000/api/Devices/{id_Device}',
                headers = headers
            )

            if not dataDevice.status_code == 200:
                logging.info("Respuesta del Dipositivo:")
                response = {"status": dataDevice.status_code, 'data': {} }
                return response

            dataDevice   = dataDevice.json()
            organization = dataDevice.get('organization')
            deviceType   = dataDevice.get('DeviceType')

            #API request
            datalocation = requests.get(
                url      = f'http://127.0.0.1:8000/api/Locations/?device={id_Device}&isActive={True}',
                headers  = headers
            )

            if not datalocation.status_code == 200:
                response = {"status": dataDevice.status_code, 'data': {}}
                logging.info("Respuesta de la ubicacion del dispositivo:", response)
                return response

            datalocation = datalocation.json()

            for location in datalocation:
                site = location.get('site')
                zone = location.get('zone')

        except Exception as e:
            logging.error('Ha ocurrido un error al consultar el DISPOSITIVO:', e)
            response = {"status": 500, 'data': e }
            return response

        #* GET KEYS FROM ZONE
        logging.info("Consultando paquetes por zona")
        try:
            dataPackageKeys = requests.get(
                url         = f'http://127.0.0.1:8000/api/PackageConfigKeys/?zone={zone}&devicetype={deviceType}',
                headers     = headers
            )

            if not dataPackageKeys.status_code == 200:
                response = {"status": dataPackageKeys.status_code, 'data': {} }
                logging.info("Respuesta al buscar las keys por Zona:", response)
                return response

            dataPackageKeys = dataPackageKeys.json()

            if not dataPackageKeys == []:

                dataKey = {}
                for data in dataPackageKeys:
                    idKey = data.get('keys')
                    keys  = requests.get(f'http://127.0.0.1:8000/api/Keys/{idKey}', headers=headers)

                    keys  = keys.json()
                    dataKey[f"{keys.get('nameKey')}"] = json.loads(str(keys.get('valueKey')))

                response = {"status": 200, 'data': dataKey }

                logging.info('LLaves encotradas')
                return response
            logging.info('LLaves no encotradas')
        except Exception as e:
            logging.error('Ha ocurrido un error al consultar las llaves por zona:', e)
            response = {"status": 500, 'data': e }
            return response

        # * GET KEYS FROM SITE
        logging.info("Consultando paquetes por Sitio")
        try:

            dataPackageKeys = requests.get(
                url     = f'http://127.0.0.1:8000/api/PackageConfigKeys/?site={site}&devicetype={deviceType}',
                headers = headers
            )

            if not dataPackageKeys.status_code == 200:
                response = {"status": dataPackageKeys.status_code, 'data': {} }
                logging.info("Respuesta al buscar las keys por Sitio:", response)
                return response

            dataPackageKeys = dataPackageKeys.json()

            if not dataPackageKeys == []:

                dataKey = {}
                for data in dataPackageKeys:
                    idKey = data.get('keys')

                    keys  = requests.get(f'http://127.0.0.1:8000/api/Keys/{idKey}',headers= headers)
                    keys  = keys.json()
                    dataKey[f"{keys.get('nameKey')}"] = json.loads(str(keys.get('valueKey')))

                response = {"status": 200, 'data': dataKey }
                logging.info('LLaves encotradas')
                return response
            logging.info('LLaves no encotradas')

        except Exception as e:
            logging.error('Ha ocurrido un error al consultar las llaves por SITIO:', e)
            response = {"status": 500, 'data': e }
            return response

        # * GET KEYS FROM ORGANIZATION
        logging.info("Consultando paquetes por Organizacion")
        try:
            dataPackageKeys = requests.get(
                url     = f'http://127.0.0.1:8000/api/PackageConfigKeys/?org={organization}&devicetype={deviceType}',
                headers = headers)

            if not dataPackageKeys.status_code == 200:
                response = {"status": dataDevice.status_code, 'data': {} }
                logging.info("Respuesta al buscar las keys por Organizacion:", response)
                return response

            dataPackageKeys = dataPackageKeys.json()

            if not dataPackageKeys == []:

                dataKey = {}
                for data in dataPackageKeys:
                    idKey = data.get('keys')

                    keys  = requests.get(f'http://127.0.0.1:8000/api/Keys/{idKey}', headers= headers)
                    keys  = keys.json()
                    dataKey[str(keys.get('nameKey'))] = json.loads(str(keys.get('valueKey')))

                response = {"status": 200, 'data': dataKey }
                logging.info('LLaves encotradas')
                return response
            logging.info('LLaves no encotradas')

        except Exception as e:
            logging.error('Ha ocurrido un error al consultar las llaves por SITIO:', e)
            response = {"status": 500, 'data': e }
            return response

    def getSettings(self,id_Device, headers):
        logging.info("-----| Consultando Settings |------")
        try:
            dataSettings = requests.get(
                url     = f'http://127.0.0.1:8000/api/Settings/?device={id_Device}',
                headers =  headers
            )

            if not dataSettings.status_code == 200:
                logging.info("No se han encontrado settings")
                response = {"status": dataSettings.status_code, 'data': [] }

                return response

            dataSettings = dataSettings.json()

            if not dataSettings == []:
                settings = []
                for data in dataSettings:
                        setting = data.get('dataSetting')
                        setting = json.loads(setting)

                        settings.append(setting)

                logging.info("Settings encontrados")
                response = {"status": 200, 'data': settings }
                return response
            else:
                logging.info("Settings no encontrados")
                response = {"status": 200, 'data': {} }

                return response
        except Exception as e:
            logging.error('Ha ocurrido un error al consultar los settings del dispositivo:', e)
            response = {"status": 500, 'data': e }
            return response

    def getApp(self,userName, app ):


        try:

            #* GET TOKEN AUTHENTICATION
            getToken = requests.post(
                url  = f'http://127.0.0.1:8000/api-token-auth/',
                json = {'username': 'root', 'password': 'root'}
            )

            if not getToken.status_code == 200:
                logging.info("No se ha podido encontrar el token:")
                response = {"status": getToken.status_code, 'data': {}}
                return response

            getToken = getToken.json()
            token    = getToken.get('token')
            headers  = {'Authorization': 'token {}'.format(token)}

            #* Get ID APLICATION
            aplication  = requests.get(
                url     = f'http://127.0.0.1:8000/api/Aplications/?app={app}',
                headers = headers
            )

            if not aplication.status_code == 200:
                logging.info("Respuesta de la aplicacion:")
                response = {"status": aplication.status_code, 'data': {} }
                return response

            aplication   = aplication.json()

            if not aplication:
                logging.info("Respuesta de la aplicacion:")
                response = {"status": aplication.status_code, 'data': {} }
                return response

            for item in aplication:
                idAplication = item.get('Id_Aplication')

            #* Get ID USER
            user  = requests.get(
                url     = f'http://127.0.0.1:8000/api/Peoples/?username={userName}',
                headers = headers
            )

            if not user.status_code == 200:
                logging.info("Respuesta del usuario:")
                response = {"status": user.status_code, 'data': {} }
                return response

            user = user.json()

            if not user:
                logging.info("Respuesta de la usuario:")
                response = {"status": user.status_code, 'data': {} }
                return response

            for item in user:
                idPeople = item.get('Id_People')

            #*Get MODULES FOR USER AND APP
            appModules  = requests.get(
                url     = f'http://127.0.0.1:8000/api/PeopleModules/?app={idAplication}&user={idPeople}',
                headers = headers
            )

            if not appModules.status_code == 200:
                logging.info("Respuesta del usuario:")
                response = {"status": appModules.status_code, 'data': {} }
                return response

            status     = appModules.status_code
            appModules = appModules.json()

            if not appModules:
                logging.info("Respuesta de los Modulos:")
                response = {"status": status, 'data': {} }
                return response


            if len(appModules)> 1:
                listModules = []
                for item in appModules:
                    listModules.append(item.get('valueModule'))

                response = {"status": status, 'data': listModules }
                return response

            for item in appModules:
                module = item.get('valueModule')

            response = {"status": status, 'data': module }
            return response


        except Exception as e:
            logging.error('Ha ocurrido un error al consultar los Modulos:', e)
            response = {"status": 500, 'data': e }
            return response
if __name__ == '__main__':
    logging.basicConfig( level = logging.INFO, format = "%(asctime)s [%(levelname)s]	%(module)s:%(lineno)d	%(funcName)s	| %(message)s" ,datefmt = '%Y-%m-%d %H:%M:%S')

    #* TEST CLASS
    manageGovernor    = ManageGovernor()
    # package, settings = manageGovernor.start(1)
    modules = manageGovernor.getApp('Pcamargo','Messaging')

    logging.info("PACKAGES --------------------")
    # logging.info(package)
    logging.info("SETTINGS --------------------")
    # logging.info(settings)
    logging.info("MODULES --------------------")
    logging.info(modules)


