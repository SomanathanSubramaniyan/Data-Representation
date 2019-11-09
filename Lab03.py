
## Somu  - Lab 03 - 09th Nov 2019
# Excercise 1
import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
print ("-------------")
print (page.content)

# Excercise 2
soup1 = BeautifulSoup(page.content,'html.parser')
print('----------')
print (soup1.tr)

# Excercise 3
with open("Lab01 - carviewer.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')
print (soup.tr)

# Excercise 4
with open("Lab01 - carviewer.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')
print (soup.tr)

# Excercise 5
rows = soup.findAll("tr")
for row in rows:
    print("-----------")
    print(row)

# Excercise 6
for row in rows:
    cols = row.findAll("td")
    for col in cols:
        print(col.text)

# Excercise 7
dataList = []
for col in cols:
    dataList.append(col.text)
    print (dataList)

# Excercise 8
employee_file = open('employee_file.csv', mode='w')
employee_writer = csv.writer(employee_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
employee_writer.writerow(['John','Accounting','November'])
employee_writer.writerow(['Eric','IT','March'])
employee_file.close()

# Excercise 9
with open("Lab01 - carviewer.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')
employee_file = open('week02data.csv', mode='w')
employee_writer = csv.writer(employee_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

rows=soup.findAll("tr")
for row in rows:
    cols = row.findAll("td")
    dataList = []
    for col in cols:
        if col.text not in (" delete"," update"):
            dataList.append(col.text)
    employee_writer.writerow(dataList)
employee_file.close()

# Excercise 10
## introduced if statement to check for the text delete and Update

# Excercise 11 and 12
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
soup = BeautifulSoup(page.content,'html.parser')
print (soup.prettify())

# Excercise 13 and 14
listings = soup.find("div", class_="PropertyListingCard")
print(listings)

# Excercise 15
price = listings.find(class_="PropertyListingCard__Price").text
print(price)

# Excercise 16
Address = listings.find(class_="PropertyListingCard__Address").text
print(Address)

# Excercise 17

listings = soup.findAll("div", class_="PropertyListingCard")

for listing in listings:
    entry = []
    price = listing.find(class_="PropertyListingCard__Price").text
    entry.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entry.append(address)
    print(entry)

# Excercise 18

page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
soup = BeautifulSoup(page.content,'html.parser')

home_file = open('week03Myhome.csv', mode='w')
home_writer = csv.writer(home_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard")

for listing in listings:
    entry = []
    price = listing.find(class_="PropertyListingCard__Price").text
    entry.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entry.append(address)

    home_writer.writerow(entry)
home_file.close()

    









