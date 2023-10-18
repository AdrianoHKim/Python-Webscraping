import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Function to retrieve and parse a web page
def retrieve_and_parse(url):
    try:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except:
        print("Error retrieving or parsing the page:", url)
        return None

# Input URL, count, and position from the user
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Loop through the specified count
for i in range(count):
    print("Retrieving:", url)

    # Retrieve and parse the current web page
    soup = retrieve_and_parse(url)
    if soup is None:
        break

    # Extract all anchor tags
    tags = soup('a')

    # Check if the position is valid
    if position <= len(tags):
        url = tags[position - 1].get('href')
    else:
        print("Position out of range, exiting.")
        break

# Extract the last name from the final URL
last_name = url.split('_')[-1].split('.')[0]
print("The answer to the assignment is:", last_name)
