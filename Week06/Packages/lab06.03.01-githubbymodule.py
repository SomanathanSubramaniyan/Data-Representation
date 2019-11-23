from github import Github 
import requests
 
g = Github("def7bc3751f6f07c2bb7393849b7c71554f44951") 
 
for repo in g.get_user().get_repos():     
    print(repo.name)

repo = g.get_repo("datarepresentationstudent/aPrivateOne") 
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url 
print (urlOfFile)

response = requests.get(urlOfFile) 
contentOfFile = response.text 
print (contentOfFile)

newContents = contentOfFile + " more stuff by Somanathan Subramaniyan \n" 
print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents ,fileInfo.sha) 
print (gitHubResponse) 

print (g.get_users())