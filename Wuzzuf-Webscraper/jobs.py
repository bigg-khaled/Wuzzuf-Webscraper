from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://wuzzuf.net/search/jobs/?q=python&a=hpb"
page = requests.get(url, timeout = 80)

soup = BeautifulSoup(page.content, 'lxml')
results = soup.find_all('div', class_='css-pkv5jc')

time = ''
with open('jobs.csv', 'w', newline='', encoding='utf8') as f:
    thewriter = writer(f)
    header = ['Title', 'Company', 'Time']
    thewriter.writerow(header)

    for result in results:
        title = result.find('h2', class_='css-m604qf').text.replace('\n', '')
        company = result.find('a', class_='css-17s97q8').text.replace('\n', '')
        time1 = result.find('div', class_='css-do6t5g')
        if time1:
            time = time1.text.replace('\n', '')
        else:
            time = "not mentioned"
        jobinfo = [title, company, time]
        thewriter.writerow(jobinfo)






