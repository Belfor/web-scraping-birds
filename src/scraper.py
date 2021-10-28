 #!/usr/bin/python
 # -*- coding: utf-8 
import requests
import csv
import unicodedata
import os
import re
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,region='ES', filename="birds.csv",limit = 5):
        self.heder = ['Orden','Familia','Género','Nombre cientifico','Citación','Referencia','Protónimo','Avibase ID','Enlace corto','Taxonmic serial name']
        self.base_url = "https://avibase.bsc-eoc.org/"
        self.search_url = self.base_url + "checklist.jsp?region=" + region
        self.filename = '../csv/' + region + '_' + filename
        self.data = []
        self.row = []
        self.limit = limit


    def extract(self):
        self.data.append(self.heder)
        self.__list_of_bird()
        self.__data2csv()

    def __list_of_bird(self):
        page = requests.get(self.search_url)
        soup = BeautifulSoup(page.content,"lxml")

        table = soup.find_all('table')[0]

        trs = table.find_all('tr')
        i = 0
    
        if len(trs) < self.limit:
            self.limit = len(trs)

        for tr in trs:
            self.row = []
            tds = tr.find_all('td')
            
            for td in tds:
                link = td.find('a')
                if link is not None:         
                    self.__info_bird(link.get("href"))
    
            if self.row:
                self.data.append(self.row)

            self.__percentage_process(i)

            i+= 1
            if i > self.limit:
                break

    def __info_bird(self,url):
        page = requests.get(self.base_url + url)
        soup = BeautifulSoup(page.content)
        taxonomy_div = soup.find(id='taxoninfo')
        paragraphs = taxonomy_div.find_all('p')

        first_element = paragraphs[0].getText()
        text = first_element.strip().replace('\n', ':').replace('\r', ':')
        attr = text.split(":")
        self.row.append(self.__normalize_string(attr[1]))
        self.row.append(self.__normalize_string(attr[3]))
        self.row.append(self.__normalize_string(attr[5]))

        for p in paragraphs[1:]:
            text = p.getText()
            attr = text.split(":")
            if attr[1].strip() != 'https':
                self.row.append(self.__normalize_string(attr[-1]))
            else:
                https = attr[1] + ':' + attr[2]
                self.row.append(self.__normalize_string(https))
      

    def __data2csv(self):
        with open(self.filename, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for row in self.data:
                writer.writerow(row)

    def __normalize_string(self,str):
        return unicodedata.normalize("NFKD",str.rstrip('\n').strip().replace('\n', ' '))

    def __percentage_process(self,i):
        self.__clear_console()
        print('processing... ' + str((i/self.limit)*100) + '%')

    def __clear_console(self):
        command = 'clear'
        if os.name in ('nt', 'dos'): 
            command = 'cls'
        os.system(command)

