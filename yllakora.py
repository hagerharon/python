import requests
from bs4 import BeautifulSoup
import csv


# get page

date_match = input("enter the date of match in the following formate MM/DD/YY")
page= requests.get(f"http://yallakora.com/Match-Center/?date={date_match}")
def main (page):
    src = page.content
    soup = BeautifulSoup(src,'lxml')
    matches_details=[]


    # get champions

    champions= soup.find_all("div",{"class":"2813 matchCard matchesList"})

    # details of every champion
    def details_match(champions):
        name_champions = champions.contents[1].find("h2").text.strip()
        Matchs_champions = champions.contents[3].find_all("li")
        number_Matchs = len(Matchs_champions)
        #******** test search in matchs of champions " 
        #  فلترة البطوﻻت مش صح مش هعرف اطلع غير ماتتشات اول بطولة محتاجة امشي ورا السيكشن 

        # print (number_Matchs)

    # details off every match 
        for i in range(number_Matchs):
            team_A = Matchs_champions[i].find("div",{"class":"teams teamA"}).text.strip()
            team_B = Matchs_champions[i].find("div",{"class":"teams teamB"}).text.strip()
            score = Matchs_champions[i].find("div",{"class":"MResult"}).find_all("span",{"class":"score"})
            type_score = f"{score[0].text.strip()} - {score[1].text.strip()}"
            time_match = Matchs_champions[i].find("div",{"class":"MResult"}).find("span",{"class":"time"}).text.strip()
        matches_details.append({"اسم البطولة":name_champions,"الفريق الأول":team_A,"الفريق الثاني":team_B,"وقت المباراة":time_match,"موعد المباراة":type_score})
        print(matches_details)
    for i in range (len(champions)):
        details_match(champions[i])
    key_table = matches_details[0].keys()
    with open("/home/hagar/Downloads/codezlla/yallakora/Matchs_details.csv","w") as outputFile:
        Table = csv.DictWriter(outputFile,key_table)
        Table.writeheader()
        Table.writerows(matches_details)
main(page)
