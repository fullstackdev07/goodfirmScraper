import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook


company_name=[]
company_rating=[]
company_tagline=[]

company_rate=[]
company_people=[]
company_year=[]
company_location=[]


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for i in range(1,650):
    url="https://www.goodfirms.co/directory/marketing-services/top-digital-marketing-companies?page="+str(i) 
    r=requests.get(url, headers=headers)
    #print(r)


    soup=BeautifulSoup(r.text, "lxml")
    #print(soup)
    name=soup.find_all("h3", class_="firm-name")
    for i in name:
        names=i.text
        company_name.append(names)
        #print(company_name)
            
    rating=soup.find_all("span", class_="rating-number")
    for i in rating:
        ratings=i.text
        company_rating.append(ratings)
        #print(company_rating)


    description=soup.find_all("div", class_="tagline")
    for i in description:
        descriptions=i.text
        company_tagline.append(descriptions)
        #print(company_tagline)

    rate=soup.find_all("div", class_="firm-pricing custom_tooltip")
    for i in rate:
        rates=i.text
        company_rate.append(rates)
        #print(company_rate)

    people=soup.find_all("div", class_="firm-employees custom_tooltip")
    for i in people:
        peoples=i.text
        company_people.append(peoples)
        #print(company_people)


    year=soup.find_all("div", class_="firm-founded custom_tooltip")
    for i in year:
        years=i.text
        company_year.append(years)
        #print(company_year)

    location=soup.find_all("div", class_="firm-location custom_tooltip")
    for i in location:
        locations=i.text
        company_location.append(locations)
        #print(company_location)



wb = Workbook()
ws = wb.active
ws.title = "goodfirms_companies"

# Write headers
ws.append(["Company Name", "Rating", "Tagline", "Rate", "People", "Year Founded", "Location"])

# Write scraped data to worksheet
for name, rating, tagline, rate, people, year, location in zip(company_name, company_rating, company_tagline, company_rate, company_people, company_year, company_location):
    ws.append([name, ratings, tagline, rate, people, year, location])

# Save the workbook
wb.save("goodfirms_companies.xlsx")
print("Scraped data has been saved to goodfirms_companies.xlsx")