import re
import requests
import json 

api_url_base = "https://geo.api.gouv.fr/communes?nom="
api_url_suite = "&fields=codeDepartement&format=json"
headers = {'Content-Type': 'application/json'}

from kalliope.core import NeuronModule

class Kalliope_version(NeuronModule):

    def __init__(self, **kwargs):
        super(Departement, self).__init__(**kwargs)
        self.nom_ville = kwargs.get("ville", None)
        # get the response of api
        api_url = '{}nom={}&{}'.format(api_url_base, self.nom_ville, api_url_suite)
        response = requests.get(api_url)

        if response.status_code == 200: 
           message = json.loads(response.content) 
        else: 
           message = "aucun retour"

        self.say(message)

