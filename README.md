
# Bulk Paper Downloader

This app help you to bulk download papers/journals you need. New update you can write your journal link list in `data.txt` file it was support for some journal/ publisher. Supported publisher:
> ieeexplore, sciencedirect, springer, aaai, acm dl & arxiv


## How To Use?

Make sure you have list of your journal/paper then put the list on list.txt file. The `list.txt` must available with `exe` file in same directory.
You can run this app by clicking the exe file as usual. Simple way you can follow this instruction

1. Set your journal link in `data.txt`
2. Run `doi.exe` it will scrape DOI list from your journal link in `data.txt`
3. Make sure everything are good for the next step
4. Run `mm.exe` to download every journal you wrote in `list.txt`

OR

You can run python file as usual

1. Clone this repository 
```bash
  git clone https://github.com/mmaul8/Bulk-Paper-Downloader.git
```
2. Make sure you have journal/paper link list in `data.txt` file
3. Run the python command in the repository folder, make sure you have all the libraries needed
```bash
  python doi.py
```
or
```bash
  python3 doi.py
```
so you will see the program will run like this image below
![App Screenshot](https://github.com/mmaul8/Bulk-Paper-Downloader/blob/main/img/doi.PNG?raw=true)

4. After complete the first step run `mm.py` file
```bash
  python mm.py
```
or
```bash
  python3 mm.py
```
And you will see the program running like the image below
![App Screenshot](https://github.com/mmaul8/Bulk-Paper-Downloader/blob/main/img/mm.PNG?raw=true)


## Hash Value Checker

- MD5 : bea0ed715e74b6a5d5b6be3d8ce61cf1
- SHA1 : 07e33d1becf98d460fb5d8e01f4de3068f19e8ea
## Badges

[![Repo Size](https://img.shields.io/github/repo-size/mmaul8/Bulk-Paper-Downloader)](https://img.shields.io/github/repo-size/mmaul8/Bulk-Paper-Downloader)

