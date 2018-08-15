import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os

# exporting to csv
f = csv.writer(open('Final_Comparisons.csv', 'w'))
f.writerow(['Bank Name','Plan Type', 'Monthly Fee','Minimum Balance to waive fee','Transaction Fee/Features'])

# BMO
print("---BMO---")

r_bmo = requests.get("https://www.bmo.com/main/personal/bank-accounts/")
c_bmo = r_bmo.content
# source code of entire bmo page
bmo_soup=BeautifulSoup(c_bmo, "html.parser")

# all the divs that have this set class
all_bmo = bmo_soup.find_all("div", {"class": "product-comparison__item"})
print("Number of plans:",len(all_bmo),"\n")
#there are 5 plans (0,1,2,3,4)
firstPrice = all_bmo[0].find("p", {"class": "compare-plan__label"}).text #testing
# print(firstPrice) #str type

for item in all_bmo:
    all_monthly_prices_bmo = item.find("p", {"class": "compare-plan__label"}).text
    type_bmo = item.find("a", {"class": "product-comparison__heading"}).text
    monthly_fee_text = item.find("span",{"class":"underlined"}).text

    print(type_bmo + " Plan")
    print(monthly_fee_text)
    print(all_monthly_prices_bmo)

    # Minimum balance to waive fee
    for waiver in item.find_all("p", {"class": "product-comparison__text"})[0]:
        print("Minimum balance to waive fee: " + waiver)
    # Number of transactions + some features
    for transacs in item.find_all("p", {"class": "product-comparison__text"})[2]:
        try:
            print("Transaction Fee/Features: " + transacs)
        except:
            pass

        f.writerow(['BMO', type_bmo, all_monthly_prices_bmo, waiver, transacs])

    print(" ")

# RBC
print("---RBC---")

r_rbc = requests.get("https://www.rbcroyalbank.com/accounts/chequing-accounts.html")
c_rbc = r_rbc.content
rbc_soup=BeautifulSoup(c_rbc, "html.parser")
all_rbc = rbc_soup.find_all("div", {"class": "grid-one-fourth"})
print("Number of plans:",len(all_rbc), "\n")

for item in all_rbc:
    type_rbc = item.find("a").text
    all_monthly_prices_rbc = item.find("i")

    print(type_rbc + " Plan")
    try:
        print(all_monthly_prices_rbc.text)
    except:
        pass
    features_rbc = item.find_all("ul",{"class":"disc-list"})
    for transacs in features_rbc:
        print("Transaction Fee/Features: " + transacs.text)

        # export to csv
        f.writerow(['RBC', type_rbc, all_monthly_prices_rbc.text, 'N/A', transacs.text])

# CIBC
print("\n---CIBC---")

r_cibc = requests.get("https://www.cibc.com/en/personal-banking/bank-accounts/chequing-accounts.html")
c_cibc = r_cibc.content
# source code of entire bmo page
cibc_soup=BeautifulSoup(c_cibc, "html.parser")

# all the divs that have this set class
all_cibc = cibc_soup.find_all("div", {"class":"small-12 medium-4 columns"})
print("Number of plans:",len(all_cibc),"\n")

for item in all_cibc:
    type_cibc = item.find("a").text
    features_cibc = item.find("div", {"class": "product-details-content"})
    all_monthly_prices_cibc = item.find_all("span", {"class": "subheading-large"})[1]
    number_of_transacs_cibc = item.find("span", {"class": "subheading-large"}).text


    print(type_cibc + " Plan\n")
    print("Monthly Fee: ", all_monthly_prices_cibc.text)
    print("Number of Transactions: " + number_of_transacs_cibc + "\n")

    # remove previous 2 print statements if you would like to un-comment the following print statement
    # print(all_features_cibc.text)

    f.writerow(['CIBC', type_cibc, all_monthly_prices_cibc.text, 'N/A', number_of_transacs_cibc])

# TD Canada
print("\n---TD Canada---")

r_td = requests.get("https://www.td.com/ca/en/personal-banking/products/bank-accounts/chequing-accounts/")
c_td = r_td.content
# source code of entire bmo page
td_soup=BeautifulSoup(c_td, "html.parser")
all_td = td_soup.find_all("div",{"class":"td-col-xs-12"})
features_td = td_soup.find_all("div",{"class":"td-product-info-row"})
print("Number of plans:",len(features_td),"\n")


for item in all_td:
    type_td = item.find("a",{"class":"td-link-standalone"})

    try:
        print("\n",type_td.text)
    except:
        pass

    for items in item.find_all("p"):
        print(items.text)

        f.writerow(['TD Canada',type_td, 'Check Features*', 'N/A', items.text])

# Scoatia Bank
print("\n---Scotia Bank---")

r_sb = requests.get("https://www.scotiabank.com/ca/en/personal/bank-accounts/chequing-accounts.html")
c_sb = r_sb.content
# source code of entire bmo page
sb_soup=BeautifulSoup(c_sb, "html.parser")
all_sb = sb_soup.find_all("div",{"class":"ss--grid-item"})
print("Number of plans:",len(all_sb),"\n")

for item in all_sb:
    type_sb = sb_soup.find("p").text
    print(type_sb)













