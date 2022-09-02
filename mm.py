import os, asyncio, requests
from tqdm import tqdm
from colorama import Fore
from bs4 import BeautifulSoup

art = """
██████╗ ██╗   ██╗██╗     ██╗  ██╗    ██████╗  █████╗ ██████╗ ███████╗██████╗          
██╔══██╗██║   ██║██║     ██║ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗         
██████╔╝██║   ██║██║     █████╔╝     ██████╔╝███████║██████╔╝█████╗  ██████╔╝         
██╔══██╗██║   ██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗         
██████╔╝╚██████╔╝███████╗██║  ██╗    ██║     ██║  ██║██║     ███████╗██║  ██║         
╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝                                                                                           
██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                    
"""

async def main():
    print(Fore.CYAN+'Membuat Folder output...')
    await asyncio.sleep(1)
    DIR = 'PDF'
    if not os.path.exists(DIR):
        os.mkdir(DIR)

    print(Fore.CYAN+'Memeriksa file list journal...')
    await asyncio.sleep(1)
    f = 'list.txt'
    if not os.path.exists(f):
        print(Fore.RED+'File list.txt tidak ditemukan!')
        await asyncio.sleep(4)
        exit()

    list = open(f, 'r')
    dois = list.readlines()
    print(Fore.GREEN+'Mulai mendownload jurnal...')
    for doi in tqdm(dois):
        try:
            name = doi.strip()
            link = 'https://sci-hub.se'
            res = requests.get(link +'/'+ doi.strip())
            soup = BeautifulSoup(res.content, 'html.parser')
            content = link + soup.find('embed').get('src').replace('#navpanes=0&view=FitH', '')
        
            req = requests.get(content, stream=True)
            with open(DIR + '/' + name.replace('/', '-') + '.pdf', 'wb') as file:
                file.write(req.content)

            pdfs = open('DOI_Ditemukan.txt', 'a')
            pdfs.write(doi.strip() + '\t' + content + '\n')
    
        except:

            ampas = open('DOI_Tidak_Ditemukan.txt', 'a')
            ampas.write(doi.strip() + '\n')

        await asyncio.sleep(1)

os.system('@echo off')
os.system('MODE 95,25')
os.system('title Bulk Paper Downloader by MAUL')
print(Fore.YELLOW+art)
print("#############################")
print("# Created by : _MMAUL_ #")
print("#############################")

if __name__ == '__main__':
    asyncio.run(main())