import requests
import json 


url = 'https://api.github.com/user/repos'
apiKey = 'def7bc3751f6f07c2bb7393849b7c71554f44951'
filename = "test"

response = requests.get(url, auth=('token',apiKey)) 
repoJSON = response.json() 


file = open(filename, 'w') 
json.dump(repoJSON, file, indent=4) 