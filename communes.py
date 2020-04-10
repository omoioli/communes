#import re
import requests
import json 
from kalliope.core import NeuronModule

api_url_base = "https://geo.api.gouv.fr/communes?nom="
api_url_suite = "&fields=nom,codesPostaux,surface,codeDepartement,departement,codeRegion,region,population&format=json"
headers = {'Content-Type': 'application/json'}

class Communes(NeuronModule):

    def __init__(self, **kwargs):
        super(Communes, self).__init__(**kwargs)
        self.ville = kwargs.get("nom_ville", None)
        
        # check if parameters have been provided
        if self._is_parameters_ok():
        
            # get the response of api
            api_url = "{}{}{}".format(api_url_base, self.ville, api_url_suite)
            response = requests.get(api_url, headers=headers)

            if response.status_code == 200: 
                jsonresult = json.loads(response.text)
                for result in jsonresult:
                    if result["nom"].lower() == self.ville.lower():
                        message = {
                            "commune_asked": self.ville,
                            "commune": jsonresult[0]["nom"],
                            "code_post": jsonresult[0]["codesPostaux"][0],
                            "surface": jsonresult[0]["surface"],
                            "population": jsonresult[0]["population"],
                            "code_department": jsonresult[0]["codeDepartement"],
                            "department": jsonresult[0]["departement"]["nom"],
                            "region": jsonresult[0]["region"]["nom"]
                            }
                        break
            else: 
                message = "no return"

            self.say(message)
            
    def _is_parameters_ok(self):
   #    """
   #    Check if received parameters are ok to perform operations in the neuron
   #    :return: true if parameters are ok, raise an exception otherwise

   #    .. raises:: MissingParameterException
   #    """
        if self.ville is None:
            raise MissingParameterException("You must specify a fr country")
       if not isinstance(self.ville, str):
            raise MissingParameterException("ville must be an string")
        return True

# Exemple JSON respnse:
#[ { "nom": "Mirande", "codesPostaux": [ "32300" ], "surface": 2365.37, "codeDepartement": "32", "codeRegion": "76", "population": 3483, "code": "32256", "_score": 1, "departement": { "code": "32", "nom": "Gers" }, "region": { "code": "76", "nom": "Occitanie" } } ]
