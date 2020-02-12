import requests
from bs4 import BeautifulSoup

def scrape_prime_ministers():
    url = 'https://en.wikipedia.org/wiki/List_of_Prime_Ministers_of_Thailand'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    tables = soup.find_all('table')

    pmtable = tables[1]
    rows = pmtable.find_all('tr')
    allpm = { }
    for row in rows[2:]:
        no = row.find_next('th').text.strip()
        if no.isnumeric() and no not in allpm:
            imgsrc = row.find_next('img')['src']
            imgurl = f'https:{imgsrc}'
            tds = row.find_all('td')
            if len(tds) > 1:
                name = tds[1].text.strip()
                if name.isnumeric() == False and len(name) > 3:
                    pm = {'imgurl': imgurl, 'name': name}
                    allpm[ no ] = pm

    return allpm

def insert(pm):
    from myapp.models import PrimeMinister
    import datetime
    p = PrimeMinister()
    p.name = pm['name']
    p.imgurl = pm['imgurl']
    p.dob = datetime.date(2010,1,1)
    p.startdate = datetime.date(2020,1,1)
    p.enddate = datetime.date(2030,1,1)
    p.party = 'ม.อบ'
    p.save()