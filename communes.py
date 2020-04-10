import re
import requests
import json 
from kalliope.core import NeuronModule

api_url_base = "https://geo.api.gouv.fr/communes?nom="
api_url_suite = "&fields=nom,codesPostaux,surface,codeDepartement,departement,codeRegion,region,population&format=json"
api_geo = "https://geo.api.gouv.fr/communes?nom=mirande&fields=codeDepartement&format=json"
headers = {'Content-Type': 'application/json'}

class Communes(NeuronModule):

    def __init__(self, **kwargs):
        super(Communes, self).__init__(**kwargs)
        self.ville = kwargs.get("nom_ville", None)
        # get the response of api
        api_url = "{}{}{}".format(api_url_base, self.ville, api_url_suite)

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200: 
         #   message = response.text
            jsonresult = json.loads(response.text)
            message = {"commune_asked": self.ville,
                       "commune": jsonresult[0]["nom"],
                       "code_post": jsonresult[0]["codesPostaux"][0],
                       "department": jsonresult[0]["departement"]["nom"],
                       "code_department": jsonresult[0]["codeDepartement"]}
        else: 
           message = "aucun retour"

        self.say(message)

#[ { "nom": "Mirande", "codesPostaux": [ "32300" ], "surface": 2365.37, "codeDepartement": "32", "codeRegion": "76", "population": 3483, "code": "32256", "_score": 1, "departement": { "code": "32", "nom": "Gers" }, "region": { "code": "76", "nom": "Occitanie" } } ]
