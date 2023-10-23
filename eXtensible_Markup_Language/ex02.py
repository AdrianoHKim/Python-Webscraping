import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter location: ")

# Fetch the XML data from the URL
try:
    data = urllib.request.urlopen(url).read()
    print("Retrieving", url)
except:
    print("Invalid URL or unable to retrieve data.")
    quit()

# Parse the XML data
tree = ET.fromstring(data)

# Find all 'count' elements
counts = tree.findall('.//count')

# Initialize a variable to keep track of the sum
total = 0

# Loop through the 'count' elements and sum their values
for count in counts:
    total += int(count.text)

# Print the count and the sum
print("Count:", len(counts))
print("Sum:", total)
