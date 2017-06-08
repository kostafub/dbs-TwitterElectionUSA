# imports
from bs4 import BeautifulSoup
import requests
import csv

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

# scraper website: (https://www.heise.de/thema/https
def main():

    fobj = open('heise.csv', 'w')      # open file
    csvw = csv.writer(fobj, delimiter = ';')      # create csv writer, set delimiter to ;

	h_https_url = "https://www.heise.de/thema/https"

        content = getPage(h_https_url).find("header")

        for c in content:
            c = c.findAll("td")
            txt = []
            for t in c:
                txt.append(t.text.encode('utf-8'))
            csvw.writerow(txt)
            #print(txt)


    fobj.close()                                # close file
    print("\nDONE !\n\n\nheise.de was scraped completely.\n")



# main program

if __name__ == '__main__':
    main()