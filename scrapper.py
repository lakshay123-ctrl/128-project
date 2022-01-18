from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)
soup = BeautifulSoup(page.text,"html.parser")
star_table = soup.find("table")
temp_list = []
table_rows = star_table.find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
star_name = []
radius = []
mass = []
distance_data = []
for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][0])
    radius.append(temp_list[i][8])
    mass.append(temp_list[i][7])
    distance_data.append(temp_list[i][5])



df = pd.DataFrame(list(zip(star_names,distance,mass,radius,luminosity)),columns = ["star_names","distance","mass","radius","luminosity"])
df.to_csv("brightstars.csv")    
    
