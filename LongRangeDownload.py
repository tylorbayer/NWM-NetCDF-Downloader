from lxml import html
import requests
import urllib2


def getFileList(config, startDate, time, geom, member):
    files = []

    url = 'https://apps.hydroshare.org/apps/nwm-data-explorer/api/GetFileList/?config=' + config + '&startDate=' + startDate + '&time=' + time + '&geom=' + geom + member
    page = requests.get(url)
    tree = html.fromstring(page.text)

## Parses html list into usable file names
    fileList = tree.xpath('//text()')
    files = fileList[0][2:-2].split('", "')

    return files

def downloadFiles(files):
## Run this block if you want to download all 120 files for given parameters
"""
    for fileName in files:
        url = 'https://apps.hydroshare.org/apps/nwm-data-explorer/api/GetFile?file=' + fileName # Downloads all files
        response = urllib2.urlopen(url)
        fileContent = response.read()

        with open(fileName, 'w') as f:
            f.write(fileContent)
"""

## Run this block if you want to download one (files[n]) of the files for given parameters
"""
    url = 'https://apps.hydroshare.org/apps/nwm-data-explorer/api/GetFile?file=' + files[0] # Downloads the first file
    response = urllib2.urlopen(url)
    fileContent = response.read()

    with open(files[0], 'w') as f:
        f.write(fileContent)
"""

### Program starts here ###

## Parameters (defaults provided)
config = "long_range" # "long_range", "medium_range" , "short_range" or "analysis_assim"
startDate = "2017-02-03" # any YYYY-MM-DD
time = "0" # "0-23" for all comma separated for individual Ex. "0,3,18"
geom = "channel" # "land", "channel", "terrain" or "reservoir"
    
## This is only for long_range files
member = "" # "" for all configs other than 'long_range'
if config == "long_range":
    member = "&member=1" # 1, 2, 3 or 4

files = getFileList(config, startDate, time, geom, member)

## **************  WARNING!!  ************** ##
## These files are very large! (About 64MB!) They will take a very long time to download ##
## They will download to whatever directory the python script is in ##
downloadFiles(files)
