import cloudscraper
import os, requests, re, json, asyncio
from colorama import Fore
from bs4 import BeautifulSoup


async def get_doi():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",}
    
    dir = 'report'
    if not os.path.exists(dir):
        os.mkdir(dir)
        print(Fore.LIGHTBLUE_EX+'Membuat Folder Report...')
        await asyncio.sleep(2)

    f = 'data.txt'
    print(Fore.LIGHTBLUE_EX+'Mengecek File data.txt...')
    if not os.path.exists(f):
        print(Fore.RED+'File data.txt tidak ditemukan!!!')
        await asyncio.sleep(3)
        exit()
    
    data = open(f, 'r')
    list = data.readlines()

    print(Fore.LIGHTBLUE_EX+'Mulai mengambil DOI...')
    for link in list:
        try:
            if 'ieeexplore' in link:
                html = requests.get(link, headers=headers, timeout=30)
                soup = BeautifulSoup(html.text, "lxml")

                doi = json.loads(re.findall(r"xplGlobal\.document\.metadata=(.*?);", str(soup.select("script")))[0])["doi"]

                print(Fore.GREEN+link.strip() + ' | '+ doi)

                log = open(dir + '/log-DOI.txt', 'a')
                log.write(link.strip() + ' | '+ doi + '\n')
            
                list = open('list.txt', 'a')
                list.write(doi + '\n')
                await asyncio.sleep(1)
        
            elif 'sciencedirect' in link:
                scraper = cloudscraper.create_scraper()
                a = scraper.get(link)
                soup = BeautifulSoup(a.content, 'html.parser')
                target = soup.find('a', class_='doi').text
                last = target.replace('https://doi.org/', '')

                print(Fore.GREEN+link.strip() + ' | '+ last)

                log = open(dir + '/log-DOI.txt', 'a')
                log.write(link.strip() + ' | '+ last + '\n')
            
                list = open('list.txt', 'a')
                list.write(last + '\n')
                await asyncio.sleep(1)

            elif 'springer' in link:
                rep = link.strip()
                a = rep.replace('https://link.springer.com/article/', '')
            
                print(Fore.GREEN+link.strip() + ' | ' + a)

                log = open(dir + '/log-DOI.txt', 'a')
                log.write(link.strip() + ' | '+ a + '\n')
            
                list = open('list.txt', 'a')
                list.write(a + '\n')
                await asyncio.sleep(1)

            else:
                print(Fore.RED+link.strip() + ' | DOI Tidak ditemukan!')
                log = open(dir + '/error-DOI.txt', 'a')
                log.write(link.strip() + ' | DOI Tidak ditemukan!' + '\n')
                await asyncio.sleep(1)

        except:

            print(Fore.RED+link.strip() + ' | Oops Something Error!!!')
            log = open(dir + '/error-DOI.txt', 'a')
            log.write(link.strip() + ' | Oops Something Error!!!' + '\n')
            await asyncio.sleep(1)

os.system('@echo off')
os.system('MODE 95,25')
os.system('title Get your DOI by _MMAUL_')
print(Fore.YELLOW+"#############################")
print("#   Created by : _MMAUL_    #")
print("#                           #")
print("#   Get DOI not their doi!  #")
print("#############################")

if __name__ == '__main__':
    asyncio.run(get_doi())