import urllib2, progressbar, csv, os
from bs4 import BeautifulSoup

# The path to the script
currentPath = os.path.dirname(os.path.abspath(__file__))

# Make the spreadsheet path
outputCsv = currentPath + '/members.csv'

# Open the file
csvFile = open(outputCsv, "wb")

# Create writer object
writer = csv.writer(csvFile, delimiter=',')

def extractMData(webpage):
    soup = BeautifulSoup(webpage)
    
    # find all the div blocks
    divBlock = soup.findAll("div", {"class":"block"})
    info = divBlock[3]
    # Extract info_left and in_right divs
    getLeft = info.findAll("div", {"class":"info_left"})
    getRight = info.findAll("div", {"class":"info_right"})
    getLeftArr = []
    getRightArr = []
    
    for i in range(0,len(getLeft)):
        textLeft = getLeft[i].get_text()
        textRight = getRight[i].get_text()
        getLeftArr.append(textLeft)
        getRightArr.append(textRight)
        
    return [getLeftArr, getRightArr]


# Open webpage
webpage = urllib2.urlopen("http://justiceleague.inadaybooks.com")

# Convert to BeautifulSoup
soup = BeautifulSoup(webpage)

# Get the contents container div
divContainer = soup.find("div", {"id":"container"})
divBlock = divContainer.findAll("div", {"class":"block"})
divSep = divBlock[3].findAll("div", {"class":"separator"})
members = divSep[3].findAll("a")

nMembers = len(members)
bar = progressbar.ProgressBar(nMembers)

count = 0

# Loop through members
for member in members:
    # Strip <a> tags
    href = member.get("href")
    # Create url to open
    url = "http://justiceleague.inadaybooks.com/"+href
    # Open url
    mPage = urllib2.urlopen(url)
    
    data = extractMData(mPage)
    
    if count == 0:
        # Write headings to csv file
        writer.writerow(data[0])
    
    writer.writerow(data[1])
    
    count+=1
    bar.update(count)