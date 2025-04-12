import json
with open ("myfile.json", "r") as json_file:
	ourjson = json.load (json.file)
print (ourjson)

print ("El token de acceso es: {}".format(ourjson["access_token"]))
print ("El token de acceso expirara en {} segundos.".format(ourjson["expires_in"]))

# Otro 7
