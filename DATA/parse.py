import requests
import csv
from bs4 import BeautifulSoup
import csv

link = 'https://mstnw.net/'

def parse(url):
  try:
    source = requests.get(url).text
  except:
    return
  soup = BeautifulSoup(source, "lxml")
  headers = soup.find_all('button', class_='nav-link')

  privilegies = headers[0].text
  anarchy = headers[1].text
  survival = headers[2].text
  tituls = headers[3].text
  advanced = headers[4].text


      
  goods_privilegies = soup.find('div', class_='tab-pane', id=privilegies)
  goods_anarchy = soup.find('div', class_='tab-pane', id=anarchy)
  goods_survival = soup.find('div', class_='tab-pane', id=survival)
  goods_tituls = soup.find('div', class_='tab-pane', id=tituls)
  goods_advanced = soup.find('div', class_='tab-pane', id=advanced)

  goods_privilegies_name = goods_privilegies.find_all('div', class_='name')
  goods_anarchy_name = goods_anarchy.find_all('div', class_='name')
  goods_survival_name = goods_survival.find_all('div', class_='name')
  goods_tituls_name = goods_tituls.find_all('div', class_='name')
  goods_advanced_name = goods_advanced.find_all('div', class_='name')

  goods_privilegies_price = goods_privilegies.find_all('div', class_='price')
  goods_anarchy_price = goods_anarchy.find_all('div', class_='price')
  goods_survival_price = goods_survival.find_all('div', class_='price')
  goods_tituls_price = goods_tituls.find_all('div', class_='price')
  goods_advanced_price = goods_advanced.find_all('div', class_='price')



  with open(f'DATA/products/{privilegies}.csv', 'w') as table:
    writer = csv.writer(table, lineterminator="\n")
    for item in range(8):
      writer.writerow(('Товар:' + goods_privilegies_name[item].text,' Цена: ' + goods_privilegies_price[item].text + 'руб.'))

  with open(f'DATA/products/{anarchy}.csv', 'w') as table:
    writer = csv.writer(table, lineterminator="\n")
    for item in range(54):
      writer.writerow(('Товар:' + goods_anarchy_name[item].text,' Цена: ' + goods_anarchy_price[item].text + 'руб.'))

  with open(f'DATA/products/{survival}.csv', 'w') as table:
    writer = csv.writer(table, lineterminator="\n")
    for item in range(53):
      writer.writerow(('Товар:' + goods_survival_name[item].text,' Цена: ' + goods_survival_price[item].text + 'руб.'))

  with open(f'DATA/products/{tituls}.csv', 'w') as table:
    writer = csv.writer(table, lineterminator="\n")
    for item in range(14):
      writer.writerow(('Товар:' + goods_tituls_name[item].text,' Цена: ' + goods_tituls_price[item].text + 'руб.'))

  with open(f'DATA/products/{advanced}.csv', 'w') as table:
    writer = csv.writer(table, lineterminator="\n")
    for item in range(5):
      writer.writerow(('Товар:' + goods_advanced_name[item].text,' Цена: ' + goods_advanced_price[item].text + 'руб.'))
def main():
  parse(link)

if __name__ == '__main__':
  main()
  
