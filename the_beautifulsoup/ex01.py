import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Prompt the user for the URL
url = input('Enter - ')
if not url:
    url = 'http://py4e-data.dr-chuck.net/comments_1912168.html'

# Open and read the HTML from the URL
html = urllib.request.urlopen(url).read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <span> tags in the HTML
tags = soup('span')

# Initialize variables for counting and summing
count = 0
total = 0

# Extract numbers from the <span> tags and compute their sum
for tag in tags:
    count += 1
    total += int(tag.contents[0])

# Print the results
print("Count", count)
print("Sum", total)