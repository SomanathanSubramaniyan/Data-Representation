import requests, json 
import json
from xlwt import *

 #url = "https://api.github.com/users?since=100" 
url = "https://api.github.com/users/andrewbeattycourseware/followers" 
response = requests.get(url) 
data = response.json() #print(data) 
#Get the file name for the new file to write 
filename = 'githubusers.json' 
with open(filename, 'w') as f:     
    json.dump(data, f, indent=4) 

w = Workbook()
ws = w.add_sheet('githubusers')
row= 0

ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
ws.write(row,4,"gravatar_id")
ws.write(row,5,"url")
ws.write(row,6,"html_url")
ws.write(row,7,"followers_url")
ws.write(row,8,"following_url")
ws.write(row,9,"gists_url")
ws.write(row,10,"starred_url")
ws.write(row,11,"subscriptions_url")
ws.write(row,12,"organizations_url")
ws.write(row,13,"repos_url")
ws.write(row,14,"events_url")
ws.write(row,15,"received_events_url")
ws.write(row,16,"type")
ws.write(row,17,"site_admin")
row +=1

for githubuser in data:
    ws.write(row,0,githubuser["login"])
    ws.write(row,1,githubuser["id"])
    ws.write(row,2,githubuser["node_id"])
    ws.write(row,3,githubuser["avatar_url"])
    ws.write(row,4,githubuser["gravatar_id"])
    ws.write(row,5,githubuser["url"])
    ws.write(row,6,githubuser["html_url"])
    ws.write(row,7,githubuser["followers_url"])
    ws.write(row,8,githubuser["following_url"])
    ws.write(row,9,githubuser["gists_url"])
    ws.write(row,10,githubuser["starred_url"])
    ws.write(row,11,githubuser["subscriptions_url"])
    ws.write(row,12,githubuser["organizations_url"])
    ws.write(row,13,githubuser["repos_url"])
    ws.write(row,14,githubuser["events_url"])
    ws.write(row,15,githubuser["received_events_url"])
    ws.write(row,16,githubuser["type"])
    ws.write(row,17,githubuser["site_admin"])
    row += 1
w.save('githubusers.xls')
