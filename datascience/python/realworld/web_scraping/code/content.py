from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup (open("files/43rd-congress.html"), features="lxml")

# print(soup.prettify())

final_link = soup.p.a
final_link.decompose()

f= csv.writer(open("files/43rd_Congress_all.csv", "w"))   # Open the output file for writing before the loop
f.writerow(["Name", "Years", "Position", "Party", "State", "Congress", "Link"]) # Write column headers as the first line

trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('a'):
        fullLink = link.get ('href')

    tds = tr.find_all("td")

    try: #we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
        names = str(tds[0].get_text()) # This structure isolate the item by its column in the table and converts it into a string.
        years = str(tds[1].get_text())
        positions = str(tds[2].get_text())
        parties = str(tds[3].get_text())
        states = str(tds[4].get_text())
        congress = tds[5].get_text()

    except:
        print("bad tr string: {}".format(tds))
        continue #This tells the computer to move on to the next item after it encounters an error

    f.writerow([names, years, positions, parties, states, congress, fullLink])

# f = csv.writer(open("43rd_Congress.csv", "w"))
# f.writerow(["Name", "Link"])    # Write column headers as the first line

# links = soup.find_all('a')
# for link in links:
#     names = link.contents[0]
#     fullLink = link.get('href')
#     # print(names)
#     # print(fullLink)

#     f.writerow([names,fullLink])